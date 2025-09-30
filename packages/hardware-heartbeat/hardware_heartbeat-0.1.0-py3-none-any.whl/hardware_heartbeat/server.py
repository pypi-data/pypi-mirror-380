import asyncio
import psutil
import subprocess
import platform
from typing import Dict, List
from mcp.server.fastmcp import FastMCP
import time

# 创建 FastMCP 实例
mcp = FastMCP("HardwareMonitor")

class HardwareMonitor:
    def __init__(self):
        self.last_net_io = psutil.net_io_counters()
        self.last_net_time = time.time()

    def get_cpu_status(self) -> Dict:
        """获取CPU状态"""
        cpu_percent = psutil.cpu_percent(interval=0.1)
        try:
            cpu_freq = psutil.cpu_freq()
            current_freq = f"{cpu_freq.current:.1f} MHz" if cpu_freq else "未知"
        except:
            current_freq = "未知"
            
        cpu_cores = psutil.cpu_count(logical=False) or 1
        cpu_threads = psutil.cpu_count(logical=True) or 1
        
        # 用通俗语言描述CPU状态
        if cpu_percent < 30:
            cpu_status = "🟢 很轻松"
            cpu_desc = f"CPU现在很闲，只用了{cpu_percent}%的力量"
        elif cpu_percent < 70:
            cpu_status = "🟡 适中"
            cpu_desc = f"CPU正在正常工作，用了{cpu_percent}%的力量"
        else:
            cpu_status = "🔴 繁忙"
            cpu_desc = f"CPU有点忙，用了{cpu_percent}%的力量，可能需要休息一下"
        
        return {
            "status": cpu_status,
            "description": cpu_desc,
            "percent": cpu_percent,
            "cores": cpu_cores,
            "threads": cpu_threads,
            "frequency": current_freq
        }

    def get_memory_status(self) -> Dict:
        """获取内存状态"""
        memory = psutil.virtual_memory()
        memory_total_gb = memory.total / (1024**3)
        memory_used_gb = memory.used / (1024**3)
        memory_percent = memory.percent
        
        # 用通俗语言描述内存状态
        if memory_percent < 60:
            memory_status = "🟢 充足"
            memory_desc = f"内存还很宽裕，用了{memory_used_gb:.1f}GB，还剩{memory_total_gb - memory_used_gb:.1f}GB空间"
        elif memory_percent < 85:
            memory_status = "🟡 适中"
            memory_desc = f"内存使用适中，用了{memory_used_gb:.1f}GB，剩余空间不多了"
        else:
            memory_status = "🔴 紧张"
            memory_desc = f"内存有点紧张！用了{memory_used_gb:.1f}GB，只剩{memory_total_gb - memory_used_gb:.1f}GB了"
        
        return {
            "status": memory_status,
            "description": memory_desc,
            "total_gb": memory_total_gb,
            "used_gb": memory_used_gb,
            "available_gb": memory.available / (1024**3),
            "percent": memory_percent
        }

    def get_disk_status(self) -> List[Dict]:
        """获取磁盘状态"""
        disks = []
        for partition in psutil.disk_partitions():
            try:
                # 跳过CD-ROM等不可用设备
                if 'cdrom' in partition.opts or partition.fstype == '':
                    continue
                    
                usage = psutil.disk_usage(partition.mountpoint)
                total_gb = usage.total / (1024**3)
                used_gb = usage.used / (1024**3)
                free_gb = usage.free / (1024**3)
                percent = usage.percent
                
                # 用通俗语言描述磁盘状态
                if percent < 70:
                    disk_status = "🟢 充足"
                    disk_desc = f"空间很充足，还剩{free_gb:.1f}GB"
                elif percent < 90:
                    disk_status = "🟡 适中"
                    disk_desc = f"空间还算够用，还剩{free_gb:.1f}GB"
                else:
                    disk_status = "🔴 紧张"
                    disk_desc = f"空间紧张！只剩{free_gb:.1f}GB了，该清理了"
                
                disks.append({
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "status": disk_status,
                    "description": disk_desc,
                    "total_gb": total_gb,
                    "used_gb": used_gb,
                    "free_gb": free_gb,
                    "percent": percent,
                    "fstype": partition.fstype
                })
            except (PermissionError, OSError):
                continue
        
        return disks

    def get_gpu_status(self) -> List[Dict]:
        """获取GPU状态 - 使用跨平台方法"""
        gpus = []
        
        try:
            # 方法1: 尝试使用nvidia-smi (Windows/Linux)
            if platform.system() == "Windows":
                result = subprocess.run([
                    'nvidia-smi', 
                    '--query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu',
                    '--format=csv,noheader,nounits'
                ], capture_output=True, text=True, timeout=10)
            else:
                result = subprocess.run([
                    'nvidia-smi', 
                    '--query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu',
                    '--format=csv,noheader,nounits'
                ], capture_output=True, text=True, timeout=10)
                
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for i, line in enumerate(lines):
                    parts = [part.strip() for part in line.split(',')]
                    if len(parts) >= 5:
                        name = parts[0]
                        utilization = float(parts[1])
                        memory_used = float(parts[2])
                        memory_total = float(parts[3])
                        temperature = float(parts[4])
                        
                        # 用通俗语言描述GPU状态
                        if utilization < 30:
                            gpu_status = "🟢 空闲"
                            gpu_desc = f"显卡现在很闲，只用了{utilization:.1f}%"
                        elif utilization < 70:
                            gpu_status = "🟡 工作中"
                            gpu_desc = f"显卡正在工作，用了{utilization:.1f}%的力量"
                        else:
                            gpu_status = "🔴 繁忙"
                            gpu_desc = f"显卡很忙！用了{utilization:.1f}%的力量"
                        
                        # 显存状态描述
                        memory_percent = (memory_used / memory_total) * 100
                        memory_desc = f"显存用了{memory_used:.0f}MB，还剩{memory_total - memory_used:.0f}MB"
                        if memory_percent > 80:
                            memory_desc += "，显存有点紧张"
                        
                        gpus.append({
                            "id": i,
                            "name": name,
                            "status": gpu_status,
                            "description": gpu_desc,
                            "load_percent": utilization,
                            "memory_used_mb": memory_used,
                            "memory_free_mb": memory_total - memory_used,
                            "memory_total_mb": memory_total,
                            "memory_percent": memory_percent,
                            "temperature": temperature,
                            "memory_description": memory_desc
                        })
                return gpus
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError, ValueError):
            # nvidia-smi 不可用，继续尝试其他方法
            pass
        
        try:
            # 方法2: 尝试使用WMIC (Windows)
            if platform.system() == "Windows":
                result = subprocess.run([
                    'wmic', 'path', 'win32_VideoController', 'get', 'Name,AdapterRAM,VideoProcessor /format:list'
                ], capture_output=True, text=True, timeout=10)
                
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    current_gpu = {}
                    for line in lines:
                        if 'Name=' in line:
                            current_gpu['name'] = line.split('=', 1)[1].strip()
                        elif 'AdapterRAM=' in line:
                            memory_bytes = int(line.split('=', 1)[1].strip())
                            current_gpu['memory_mb'] = memory_bytes / (1024*1024) if memory_bytes else 0
                    
                    if current_gpu.get('name'):
                        gpus.append({
                            "id": 0,
                            "name": current_gpu['name'],
                            "status": "⚪ 基本信息",
                            "description": "检测到显卡，但无法获取实时使用情况",
                            "load_percent": 0,
                            "memory_used_mb": 0,
                            "memory_free_mb": current_gpu.get('memory_mb', 0),
                            "memory_total_mb": current_gpu.get('memory_mb', 0),
                            "memory_percent": 0,
                            "temperature": 0,
                            "memory_description": f"显存总量: {current_gpu.get('memory_mb', 0):.0f}MB"
                        })
                        return gpus
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError, ValueError):
            pass
        
        # 如果所有方法都失败，返回基础信息
        gpus.append({
            "id": 0,
            "name": "未知显卡",
            "status": "⚫ 未知",
            "description": "无法获取显卡详细信息，可能没有独立显卡或需要安装显卡驱动",
            "load_percent": 0,
            "memory_used_mb": 0,
            "memory_free_mb": 0,
            "memory_total_mb": 0,
            "memory_percent": 0,
            "temperature": 0,
            "memory_description": "需要安装NVIDIA驱动或使用兼容的显卡"
        })
        
        return gpus

    def get_network_status(self) -> Dict:
        """获取网络状态"""
        current_net_io = psutil.net_io_counters()
        current_time = time.time()
        time_diff = current_time - self.last_net_time
        
        if time_diff > 0:
            # 计算网速
            upload_speed = (current_net_io.bytes_sent - self.last_net_io.bytes_sent) / time_diff
            download_speed = (current_net_io.bytes_recv - self.last_net_io.bytes_recv) / time_diff
        else:
            upload_speed = 0
            download_speed = 0
        
        # 更新上一次的数据
        self.last_net_io = current_net_io
        self.last_net_time = current_time
        
        # 用通俗语言描述网络状态
        upload_speed_mbps = upload_speed / 1024 / 1024 * 8
        download_speed_mbps = download_speed / 1024 / 1024 * 8
        
        if download_speed_mbps < 1:
            net_status = "🌐 空闲"
            net_desc = f"网络很安静，下载速度{download_speed_mbps:.2f} Mbps"
        elif download_speed_mbps < 10:
            net_status = "🌐 正常"
            net_desc = f"网络正常使用中，下载速度{download_speed_mbps:.2f} Mbps"
        else:
            net_status = "🌐 繁忙"
            net_desc = f"网络正在高速传输，下载速度{download_speed_mbps:.2f} Mbps"
        
        return {
            "status": net_status,
            "description": net_desc,
            "upload_speed_mbps": upload_speed_mbps,
            "download_speed_mbps": download_speed_mbps,
            "bytes_sent": current_net_io.bytes_sent,
            "bytes_recv": current_net_io.bytes_recv
        }

    def get_system_info(self) -> Dict:
        """获取系统信息"""
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        uptime_hours = uptime_seconds / 3600
        
        # 用通俗语言描述运行时间
        if uptime_hours < 1:
            uptime_desc = f"系统刚刚启动{uptime_seconds/60:.0f}分钟"
        elif uptime_hours < 24:
            uptime_desc = f"系统已经运行了{uptime_hours:.1f}小时"
        else:
            uptime_days = uptime_hours / 24
            uptime_desc = f"系统已经连续工作{uptime_days:.1f}天了"
        
        return {
            "boot_time": boot_time,
            "uptime_seconds": uptime_seconds,
            "uptime_description": uptime_desc,
            "platform": f"{platform.system()} {platform.release()}"
        }

# 创建全局实例
hardware_monitor = HardwareMonitor()

def _format_hardware_report(cpu, memory, disks, gpus, network, system) -> str:
    """格式化硬件状态报告"""
    result = ["💻 电脑硬件状态报告", ""]
    
    # CPU信息
    result.append("🚀 **CPU处理器**")
    result.append(f"   {cpu['description']}")
    result.append(f"   📊 使用率: {cpu['percent']}% | 核心: {cpu['cores']}核{cpu['threads']}线程")
    if cpu['frequency'] != "未知":
        result.append(f"   ⚡ 频率: {cpu['frequency']}")
    result.append("")
    
    # 内存信息
    result.append("🧠 **内存**")
    result.append(f"   {memory['description']}")
    result.append(f"   📊 使用率: {memory['percent']}% | 总量: {memory['total_gb']:.1f}GB")
    result.append("")
    
    # 磁盘信息
    result.append("💾 **磁盘存储**")
    for disk in disks[:3]:  # 只显示前3个磁盘
        result.append(f"   {disk['device']} ({disk['mountpoint']}) - {disk['status']}")
        result.append(f"   {disk['description']}")
        result.append(f"   📊 使用率: {disk['percent']}% | 总量: {disk['total_gb']:.1f}GB")
    if not disks:
        result.append("   无法获取磁盘信息")
    result.append("")
    
    # GPU信息
    result.append("🎮 **显卡**")
    for gpu in gpus:
        result.append(f"   {gpu['name']} - {gpu['status']}")
        result.append(f"   {gpu['description']}")
        result.append(f"   {gpu['memory_description']}")
        if gpu['temperature'] > 0:
            result.append(f"   🌡️ 温度: {gpu['temperature']}°C")
    result.append("")
    
    # 网络信息
    result.append("🌐 **网络**")
    result.append(f"   {network['description']}")
    result.append(f"   ⬆️ 上传: {network['upload_speed_mbps']:.2f} Mbps")
    result.append(f"   ⬇️ 下载: {network['download_speed_mbps']:.2f} Mbps")
    result.append("")
    
    # 系统信息
    result.append("⚙️ **系统信息**")
    result.append(f"   {system['uptime_description']}")
    result.append(f"   🖥️ 平台: {system['platform']}")
    
    return "\n".join(result)

@mcp.tool()
async def get_hardware_status() -> str:
    """获取完整的硬件状态报告
    
    用通俗易懂的语言告诉你电脑的CPU、内存、硬盘、显卡等硬件的当前状态
    """
    try:
        # 获取各种硬件信息
        cpu = hardware_monitor.get_cpu_status()
        memory = hardware_monitor.get_memory_status()
        disks = hardware_monitor.get_disk_status()
        gpus = hardware_monitor.get_gpu_status()
        network = hardware_monitor.get_network_status()
        system = hardware_monitor.get_system_info()
        
        return _format_hardware_report(cpu, memory, disks, gpus, network, system)
    except Exception as e:
        return f"❌ 获取硬件状态失败: {str(e)}"

@mcp.tool()
async def get_cpu_status() -> str:
    """专门查看CPU处理器的状态
    
    告诉你CPU现在忙不忙，用了多少力量在工作
    """
    try:
        cpu = hardware_monitor.get_cpu_status()
        result = [
            "🚀 **CPU处理器状态**",
            f"   {cpu['description']}",
            f"   📊 使用率: {cpu['percent']}%",
            f"   🏗️ 核心数: {cpu['cores']}物理核心 + {cpu['threads'] - cpu['cores']}逻辑核心 = {cpu['threads']}线程",
        ]
        if cpu['frequency'] != "未知":
            result.append(f"   ⚡ 运行频率: {cpu['frequency']}")
        return "\n".join(result)
    except Exception as e:
        return f"❌ 获取CPU状态失败: {str(e)}"

@mcp.tool()
async def get_memory_status() -> str:
    """专门查看内存状态
    
    告诉你内存用了多少，还剩多少空间
    """
    try:
        memory = hardware_monitor.get_memory_status()
        result = [
            "🧠 **内存状态**",
            f"   {memory['description']}",
            f"   📊 使用率: {memory['percent']}%",
            f"   💾 总量: {memory['total_gb']:.1f} GB",
            f"   ✅ 已用: {memory['used_gb']:.1f} GB", 
            f"   💰 可用: {memory['available_gb']:.1f} GB"
        ]
        return "\n".join(result)
    except Exception as e:
        return f"❌ 获取内存状态失败: {str(e)}"

@mcp.tool()
async def get_gpu_status() -> str:
    """专门查看显卡状态
    
    告诉你显卡忙不忙，显存用了多少
    """
    try:
        gpus = hardware_monitor.get_gpu_status()
        result = ["🎮 **显卡状态**"]
        
        for gpu in gpus:
            result.append(f"   **{gpu['name']}** - {gpu['status']}")
            result.append(f"   {gpu['description']}")
            result.append(f"   {gpu['memory_description']}")
            if gpu['load_percent'] > 0:
                result.append(f"   📊 GPU使用率: {gpu['load_percent']:.1f}%")
            if gpu['memory_total_mb'] > 0:
                result.append(f"   🎯 显存总量: {gpu['memory_total_mb']:.0f}MB")
            if gpu['temperature'] > 0:
                result.append(f"   🌡️ 温度: {gpu['temperature']}°C")
            result.append("")
        
        return "\n".join(result).strip()
    except Exception as e:
        return f"❌ 获取显卡状态失败: {str(e)}"

@mcp.tool()
async def get_disk_status() -> str:
    """查看磁盘存储空间
    
    告诉你各个硬盘分区用了多少空间，还剩多少
    """
    try:
        disks = hardware_monitor.get_disk_status()
        result = ["💾 **磁盘存储状态**"]
        
        for disk in disks:
            result.append(f"   **{disk['device']}** ({disk['mountpoint']}) - {disk['status']}")
            result.append(f"   {disk['description']}")
            result.append(f"   📊 使用率: {disk['percent']}%")
            result.append(f"   💽 空间: {disk['used_gb']:.1f}GB / {disk['total_gb']:.1f}GB (剩余 {disk['free_gb']:.1f}GB)")
            result.append(f"   🗂️ 文件系统: {disk['fstype']}")
            result.append("")
        
        if not disks:
            result.append("   无法获取磁盘信息")
            
        return "\n".join(result)
    except Exception as e:
        return f"❌ 获取磁盘状态失败: {str(e)}"

@mcp.tool()
async def get_quick_status() -> str:
    """快速查看电脑核心状态
    
    用最简洁的方式告诉你CPU、内存、显卡的关键状态
    """
    try:
        cpu = hardware_monitor.get_cpu_status()
        memory = hardware_monitor.get_memory_status()
        gpus = hardware_monitor.get_gpu_status()
        
        gpu_status = "未使用或不可用"
        if gpus and gpus[0]['load_percent'] > 0:
            gpu_status = f"{gpus[0]['status']} ({gpus[0]['load_percent']:.1f}%)"
        elif gpus:
            gpu_status = f"{gpus[0]['status']}"
            
        result = [
            "⚡ **电脑快速状态**",
            "",
            f"🚀 CPU: {cpu['status']} ({cpu['percent']}%)",
            f"🧠 内存: {memory['status']} ({memory['percent']}%)", 
            f"🎮 显卡: {gpu_status}",
            "",
            "💡 提示: 使用 get_hardware_status 查看详细报告"
        ]
        
        return "\n".join(result)
    except Exception as e:
        return f"❌ 获取快速状态失败: {str(e)}"

@mcp.tool()
async def monitor_resources(duration: int = 10, interval: int = 2) -> str:
    """监控硬件资源变化
    
    Args:
        duration: 监控总时长(秒)，默认10秒
        interval: 采样间隔(秒)，默认2秒
    """
    try:
        if duration > 60:
            return "❌ 监控时长不能超过60秒"
        if interval < 1:
            return "❌ 采样间隔不能小于1秒"
            
        result = [f"📈 **开始监控硬件资源 ({duration}秒)**", ""]
        
        samples = duration // interval
        for i in range(samples):
            cpu = hardware_monitor.get_cpu_status()
            memory = hardware_monitor.get_memory_status()
            
            result.append(f"⏱️ 第 {i*interval} 秒:")
            result.append(f"   CPU: {cpu['percent']}% - {cpu['status']}")
            result.append(f"   内存: {memory['percent']}% - {memory['status']}")
            result.append("")
            
            if i < samples - 1:  # 不是最后一次循环
                await asyncio.sleep(interval)
        
        result.append("📊 **监控结束**")
        return "\n".join(result)
    except Exception as e:
        return f"❌ 监控过程中出错: {str(e)}"

# 主入口函数
def main():
    """主入口函数"""
    print("💻 硬件状态监控MCP服务器启动中...")
    print("📋 可用工具:")
    print("   - get_hardware_status: 获取完整硬件状态报告")
    print("   - get_quick_status: 快速查看核心状态") 
    print("   - get_cpu_status: 专门查看CPU状态")
    print("   - get_memory_status: 专门查看内存状态")
    print("   - get_gpu_status: 专门查看显卡状态")
    print("   - get_disk_status: 专门查看磁盘状态")
    print("   - monitor_resources: 监控硬件资源变化")
    
    # 使用stdio传输运行MCP服务器
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()