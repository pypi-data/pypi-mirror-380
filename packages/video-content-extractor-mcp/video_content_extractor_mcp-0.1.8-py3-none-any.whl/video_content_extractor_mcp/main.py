from mcp.server.fastmcp import FastMCP, Context
import ffmpeg
import os  # For checking file existence if needed, though ffmpeg handles it
import shutil  # For cleaning up temporary directories
import logging
from logging.handlers import RotatingFileHandler
import uuid
import glob
import re
import tempfile
import threading
import time
import subprocess
from pathlib import Path



# 配置日志输出到stderr，避免干扰MCP通信
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 防止 basicConfig 被早期初始化抵消

# 使用用户临时目录存放日志文件
log_dir = Path(tempfile.gettempdir()) / "video-content-extractor-mcp"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "debug.log"

file_handler = RotatingFileHandler(str(log_file), maxBytes=5_000_000, backupCount=3, encoding="utf-8")

file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.propagate = False

FFMPEG_BINARY = os.environ.get('FFMPEG_BINARY', 'ffmpeg')
FFPROBE_BINARY = os.environ.get('FFPROBE_BINARY', 'ffprobe')


# --- ffmpeg/ffprobe helpers that always use resolved binaries ---
def _ffmpeg_run(stream_spec, **kwargs):
    """Run ffmpeg with an explicit binary path to avoid env propagation issues."""
    if 'overwrite_output' not in kwargs:
        kwargs['overwrite_output'] = True
    return ffmpeg.run(stream_spec, cmd=FFMPEG_BINARY, **kwargs)


def _ffmpeg_run_async(stream_spec, **kwargs):
    """Run ffmpeg asynchronously with explicit binary path."""
    return ffmpeg.run_async(stream_spec, cmd=FFMPEG_BINARY, **kwargs)


def _ffprobe_probe(path: str, **kwargs):
    """Probe media with explicit ffprobe binary."""
    return ffmpeg.probe(path, cmd=FFPROBE_BINARY, **kwargs)


def _ffmpeg_run_with_progress(stream_spec, operation_name: str = "Processing", ctx: Context = None, **kwargs):
    """Run ffmpeg with progress notifications to prevent timeout."""
    if 'overwrite_output' not in kwargs:
        kwargs['overwrite_output'] = True
    
    # Start ffmpeg process asynchronously
    process = _ffmpeg_run_async(stream_spec, pipe_stderr=True, **kwargs)
    
    # Progress monitoring thread
    def monitor_progress():
        if ctx:
            progress = 0
            while process.poll() is None:
                ctx.report_progress(progress, f"{operation_name}... {progress}%")
                time.sleep(2)  # Report progress every 2 seconds
                progress = min(progress + 10, 90)  # Increment progress up to 90%
            
            # Final progress report
            if process.returncode == 0:
                ctx.report_progress(100, f"{operation_name} completed successfully")
            else:
                ctx.report_progress(100, f"{operation_name} failed")
    
    # Start monitoring thread if context is provided
    if ctx:
        monitor_thread = threading.Thread(target=monitor_progress, daemon=True)
        monitor_thread.start()
    
    # Wait for process to complete
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        error_message = stderr.decode('utf8') if stderr else "Unknown error"
        raise ffmpeg.Error('ffmpeg', stdout, stderr)
    
    return process


def _prepare_path(input_path: str, output_path: str) -> None:
    if not os.path.exists(input_path):
        raise RuntimeError(f"Error: Input file not found at {input_path}")
    try:
        parent_dir = os.path.dirname(output_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Error creating output directory for {output_path}: {str(e)}")
    if os.path.exists(output_path):
        raise RuntimeError(
            f"Error: Output file already exists at {output_path}. Please choose a different path or delete the existing file.")

def _prepare_path_for_dir(input_path: str, output_dir: str) -> None:
    """Prepare paths for directory output (doesn't check if output directory exists since it's expected to exist or be created)."""
    if not os.path.exists(input_path):
        raise RuntimeError(f"Error: Input file not found at {input_path}")
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Error creating output directory {output_dir}: {str(e)}")


# Create an MCP server instance
mcp = FastMCP("VideoMaterialExtraction")


@mcp.tool()
def extract_audio_from_video(video_path: str, output_audio_path: str, audio_codec: str = 'mp3', ctx: Context = None) -> str:
    """从视频文件中提取音频。

    Args:
        video_path: 输入视频文件路径。
        output_audio_path: 输出音频文件路径。
        audio_codec: 音频编码格式（如 'mp3'、'aac'、'wav'、'flac'）。

    Returns:
        A status message indicating success or failure.
    """
    _prepare_path(video_path, output_audio_path)
    # 校验音频编码格式
    valid_codecs = {'mp3', 'aac', 'wav', 'flac', 'm4a', 'ogg', 'wma'}
    if audio_codec not in valid_codecs:
        raise RuntimeError(f"Error: Invalid audio_codec '{audio_codec}'. Supported: {', '.join(sorted(valid_codecs))}")

    # 检查输入文件
    if not os.path.exists(video_path):
        raise RuntimeError(f"Error: Input video file not found at {video_path}")
    try:
        logger.info(f"抽取视频 {video_path} 中的音频到 {output_audio_path} ，音频格式 {audio_codec}")
        try:
            exists = os.path.exists(video_path)
            readable = os.access(video_path, os.R_OK)
            size = os.path.getsize(video_path) if exists else 'N/A'
            logger.info(f"输入文件检查: exists={exists} readable={readable} size={size}")
        except Exception as _e:
            logger.info(f"输入文件检查失败: {str(_e)}")
        
        if ctx:
            ctx.report_progress(0, "开始提取音频...")
        
        input_stream = ffmpeg.input(video_path)
        output_stream = input_stream.output(output_audio_path, acodec=audio_codec)
        _ffmpeg_run_with_progress(output_stream, operation_name="音频提取")
        return f"Audio extracted successfully to {output_audio_path}"
    except ffmpeg.Error as e:
        error_message = e.stderr.decode('utf8') if e.stderr else str(e)
        raise RuntimeError(f"Error extracting audio: {error_message}")
    except FileNotFoundError as e:
        # 可能是 ffmpeg 可执行文件未找到，也可能是输入文件不存在
        msg = str(e)
        logger.info(f"FileNotFoundError: {msg}")
        logger.info(f"os.path.basename(FFMPEG_BINARY): {os.path.basename(FFMPEG_BINARY)}")
        if isinstance(FFMPEG_BINARY, str) and (FFMPEG_BINARY in msg or os.path.basename(FFMPEG_BINARY) in msg):
            raise RuntimeError(f"Error: ffmpeg 可执行文件未找到或不可执行。当前设置 FFMPEG_BINARY={FFMPEG_BINARY}")
        raise RuntimeError(f"Error: Input video file not found at {video_path}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")


@mcp.tool()
def trim_video(video_path: str, output_video_path: str, start_time: str, end_time: str, ctx: Context = None) -> str:
    """按指定时间范围裁剪视频片段。

    Args:
        video_path: 输入视频文件路径。
        output_video_path: 输出视频文件路径。
        start_time: 开始时间（支持 'HH:MM:SS' 或秒数）。
        end_time: 结束时间（支持 'HH:MM:SS' 或秒数）。

    Returns:
        A status message indicating success or failure.
    """
    _prepare_path(video_path, output_video_path)
    # 简单时间格式校验
    import re
    for time_val, name in [(start_time, 'start_time'), (end_time, 'end_time')]:
        if not re.match(r'^\d+(\.\d+)?$|^\d{1,2}:\d{2}:\d{2}(\.\d+)?$', str(time_val)):
            raise RuntimeError(f"Error: Invalid {name} format '{time_val}'. Expected 'HH:MM:SS' or seconds.")
    try:
        if ctx:
            ctx.report_progress(0, "开始裁剪视频...")
        
        input_stream = ffmpeg.input(video_path, ss=start_time, to=end_time)
        # Attempt to copy codecs to avoid re-encoding if possible
        output_stream = input_stream.output(output_video_path, c='copy')
        _ffmpeg_run_with_progress(output_stream, ctx=ctx, operation_name="视频裁剪")
        return f"Video trimmed successfully (codec copy) to {output_video_path}"
    except ffmpeg.Error as e:
        error_message_copy = e.stderr.decode('utf8') if e.stderr else str(e)
        try:
            # Fallback to re-encoding if codec copy fails
            input_stream_recode = ffmpeg.input(video_path, ss=start_time, to=end_time)
            output_stream_recode = input_stream_recode.output(output_video_path)
            _ffmpeg_run_with_progress(output_stream_recode, ctx=ctx, operation_name="视频裁剪")
            return f"Video trimmed successfully (re-encoded) to {output_video_path}"
        except ffmpeg.Error as e_recode:
            error_message_recode = e_recode.stderr.decode('utf8') if e_recode.stderr else str(e_recode)
            raise RuntimeError(
                f"Error trimming video. Copy attempt: {error_message_copy}. Re-encode attempt: {error_message_recode}")
    except FileNotFoundError:
        raise RuntimeError(f"Error: Input video file not found at {video_path}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")


@mcp.tool()
def extract_video_frames(
        video_path: str,
        output_dir: str,
        image_format: str = "png",
        interval_seconds: float | None = None,
        extract_first: bool = False,
        extract_last: bool = False,
        width: int | None = None,
        height: int | None = None,
        ctx: Context = None,
) -> str:
    """从视频中按间隔或特定位置提取帧为图片。

    Args:
        video_path: 输入视频路径。
        output_dir: 输出目录（会自动创建）。
        image_format: 输出图片格式，如 'png'|'jpg'|'webp'。默认 'png'。
        interval_seconds: 间隔秒数；大于 0 时启用按间隔提取。
        extract_first: 是否额外导出首帧。
        extract_last: 是否额外导出末帧。
        width: 可选，缩放输出宽度。
        height: 可选，缩放输出高度。

    Returns:
        A status message indicating success or failure.
    """
    _prepare_path_for_dir(video_path, output_dir)
    # 校验图片格式
    valid_formats = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'tiff'}
    if image_format not in valid_formats:
        raise RuntimeError(
            f"Error: Invalid image_format '{image_format}'. Supported: {', '.join(sorted(valid_formats))}")

    # 校验间隔参数
    if interval_seconds is not None and interval_seconds <= 0:
        raise RuntimeError("Error: interval_seconds must be positive.")

    # 校验尺寸参数
    if width is not None and width <= 0:
        raise RuntimeError("Error: width must be positive.")
    if height is not None and height <= 0:
        raise RuntimeError("Error: height must be positive.")
    try:
        if not (interval_seconds and interval_seconds > 0) and not extract_first and not extract_last:
            raise RuntimeError("Error: 需至少指定一种提取方式（interval_seconds>0 或 extract_first/extract_last 任一）。")

        # 统一的文件前缀，避免与既有文件冲突
        prefix = f"frames_{uuid.uuid4().hex[:8]}"
        created_files: list[str] = []

        # 可选获取视频时长（末帧提取需要）
        video_duration_sec = None
        if extract_last:
            try:
                probe = _ffprobe_probe(video_path)
                video_duration_sec = float(probe["format"]["duration"]) if "format" in probe and "duration" in probe[
                    "format"] else None
            except Exception:
                video_duration_sec = None

        # 1) 按固定时间间隔导出
        if interval_seconds and interval_seconds > 0:
            if ctx:
                ctx.report_progress(10, "开始按间隔提取帧...")
            fps_val = 1.0 / float(interval_seconds)
            input_stream = ffmpeg.input(video_path)
            v = input_stream.video.filter("fps", fps=fps_val)
            if width or height:
                scale_w = width if width else -1
                scale_h = height if height else -1
                v = v.filter("scale", scale_w, scale_h)
            pattern = os.path.join(output_dir, f"{prefix}_%06d.{image_format}")
            _ffmpeg_run_with_progress(ffmpeg.output(v, pattern, vsync="vfr"), ctx=ctx, operation_name="间隔帧提取")
            created_files.extend(sorted(glob.glob(os.path.join(output_dir, f"{prefix}_*.{image_format}"))))

        # 2) 首帧导出
        if extract_first:
            if ctx:
                ctx.report_progress(50, "提取首帧...")
            first_path = os.path.join(output_dir, f"{prefix}_first.{image_format}")
            v1 = ffmpeg.input(video_path, ss=0)
            vf = v1.video
            if width or height:
                scale_w = width if width else -1
                scale_h = height if height else -1
                vf = vf.filter("scale", scale_w, scale_h)
            _ffmpeg_run(ffmpeg.output(vf, first_path, vframes=1), capture_stdout=True, capture_stderr=True)
            created_files.append(first_path)

        # 3) 末帧导出（取接近末尾的一帧，避免 EOF 边界）
        if extract_last:
            if ctx:
                ctx.report_progress(80, "提取末帧...")
            if video_duration_sec is None or video_duration_sec <= 0:
                raise RuntimeError("Error: Failed to resolve video duration for last-frame extraction.")
            # 留出 10ms 作为缓冲，确保命中末尾有效帧
            last_ts = max(video_duration_sec - 0.01, 0)
            last_path = os.path.join(output_dir, f"{prefix}_last.{image_format}")
            v2 = ffmpeg.input(video_path, ss=last_ts)
            vf2 = v2.video
            if width or height:
                scale_w = width if width else -1
                scale_h = height if height else -1
                vf2 = vf2.filter("scale", scale_w, scale_h)
            _ffmpeg_run(ffmpeg.output(vf2, last_path, vframes=1), capture_stdout=True, capture_stderr=True)
            created_files.append(last_path)

        if not created_files:
            raise RuntimeError("Error: No frames were produced. Please check parameters.")

        if ctx:
            ctx.report_progress(100, "帧提取完成")

        return (
            f"Frames extracted successfully. Count={len(created_files)}. "
            f"Output dir='{output_dir}', prefix='{prefix}'."
        )
    except ffmpeg.Error as e:
        error_message = e.stderr.decode('utf8') if e.stderr else str(e)
        raise RuntimeError(f"Error extracting frames: {error_message}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred in extract_video_frames: {str(e)}")


@mcp.tool()
def extract_scene_change_frames(
        video_path: str,
        output_dir: str,
        image_format: str = "png",
        scene_threshold: float = 0.4,
        min_scene_gap_seconds: float | None = None,
        max_frames: int | None = None,
        width: int | None = None,
        height: int | None = None,
        ctx: Context = None,
) -> str:
    """基于画面变化检测提取场景切换关键帧。

    Args:
        video_path: 输入视频路径。
        output_dir: 输出目录（会自动创建）。
        image_format: 输出图片格式，如 'png'|'jpg'|'webp'。默认 'png'。
        scene_threshold: 场景变化阈值（0.0~1.0，典型值 0.3~0.5）。
        min_scene_gap_seconds: 连续关键帧之间的最小时间间隔。
        max_frames: 最多导出的关键帧数量。
        width: 可选，缩放输出宽度。
        height: 可选，缩放输出高度。

    Returns:
        A status message indicating success or failure.
    """
    _prepare_path_for_dir(video_path, output_dir)
    # 校验参数
    valid_formats = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'tiff'}
    if image_format not in valid_formats:
        raise RuntimeError(
            f"Error: Invalid image_format '{image_format}'. Supported: {', '.join(sorted(valid_formats))}")

    if not (0.0 <= scene_threshold <= 1.0):
        raise RuntimeError(f"Error: scene_threshold must be between 0.0 and 1.0, got {scene_threshold}")

    if min_scene_gap_seconds is not None and min_scene_gap_seconds <= 0:
        raise RuntimeError("Error: min_scene_gap_seconds must be positive.")

    if max_frames is not None and max_frames <= 0:
        raise RuntimeError("Error: max_frames must be positive.")

    if width is not None and width <= 0:
        raise RuntimeError("Error: width must be positive.")
    if height is not None and height <= 0:
        raise RuntimeError("Error: height must be positive.")
    try:

        # 获取视频时长，末尾边界安全
        duration = None
        try:
            probe = _ffprobe_probe(video_path)
            duration = float(probe["format"].get("duration", 0.0)) if "format" in probe else None
        except Exception:
            duration = None

        if ctx:
            ctx.report_progress(10, "开始检测场景变化...")
        
        # 第一遍：用 select+showinfo 找到候选时间戳
        detect_spec = (
            ffmpeg
            .input(video_path)
            .video
            .filter("select", f"gt(scene,{scene_threshold})")
            .filter("showinfo")
            .output("-", format="null")
        )
        detect_proc = _ffmpeg_run_async(detect_spec, pipe_stderr=True)
        _, stderr_bytes = detect_proc.communicate()
        stderr_str = stderr_bytes.decode("utf8")

        # showinfo 行内形如 ... pts_time:12.345 ...
        times = [float(x) for x in re.findall(r"pts_time:(\d+(?:\.\d+)?)", stderr_str)]
        if not times:
            return "No scene-change frames detected."

        # 二次去重：最小间隔
        filtered_times: list[float] = []
        last_kept = None
        gap = float(min_scene_gap_seconds) if (min_scene_gap_seconds and min_scene_gap_seconds > 0) else None
        for t in sorted(times):
            if duration is not None:
                t = min(max(t, 0.0), max(duration - 0.01, 0.0))
            if last_kept is None:
                filtered_times.append(t)
                last_kept = t
                continue
            if gap is None or (t - last_kept) >= gap:
                filtered_times.append(t)
                last_kept = t

        # 限制最大数量
        if max_frames and max_frames > 0:
            filtered_times = filtered_times[:max_frames]

        if not filtered_times:
            return "No scene-change frames after gap/limit filtering."

        prefix = f"scenes_{uuid.uuid4().hex[:8]}"
        created_files: list[str] = []

        if ctx:
            ctx.report_progress(50, "开始提取场景关键帧...")
        
        # 第二遍：逐时间戳抽帧
        for idx, ts in enumerate(filtered_times, start=1):
            out_path = os.path.join(output_dir, f"{prefix}_{idx:06d}.{image_format}")
            inp = ffmpeg.input(video_path, ss=ts)
            vf = inp.video
            if width or height:
                scale_w = width if width else -1
                scale_h = height if height else -1
                vf = vf.filter("scale", scale_w, scale_h)
            _ffmpeg_run(ffmpeg.output(vf, out_path, vframes=1), capture_stdout=True, capture_stderr=True)
            created_files.append(out_path)
            
            if ctx:
                progress = 50 + int((idx / len(filtered_times)) * 40)
                ctx.report_progress(progress, f"已提取 {idx}/{len(filtered_times)} 帧...")

        if ctx:
            ctx.report_progress(100, "场景关键帧提取完成")
        
        return (
            f"Scene-change frames extracted. Count={len(created_files)}. "
            f"Output dir='{output_dir}', prefix='{prefix}'."
        )
    except ffmpeg.Error as e:
        error_message = e.stderr.decode('utf8') if e.stderr else str(e)
        raise RuntimeError(f"Error extracting scene-change frames: {error_message}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred in extract_scene_change_frames: {str(e)}")


def main():
    """Main entry point for the MCP server."""
    mcp.run()


# Main execution block to run the server
if __name__ == "__main__":
    main()