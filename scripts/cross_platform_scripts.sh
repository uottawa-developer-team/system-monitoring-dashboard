# Function to collect CPU usage
collect_cpu_usage() {
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    top -b -n 1 | grep "Cpu(s)" > cpu_usage.txt
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    top -l 1 | grep "CPU usage" > cpu_usage.txt
  elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    powershell.exe -Command "Get-Counter -Counter \"\\Processor(_Total)\\% Processor Time\" | Select-Object -ExpandProperty CounterSamples | Select-Object -ExpandProperty CookedValue" > cpu_usage.txt
  fi
}

# Function to collect memory usage
collect_memory_usage() {
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    free -m > memory_usage.txt
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    vm_stat > memory_usage.txt
  elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    powershell.exe -Command "Get-Counter -Counter \"\\Memory\\Available MBytes\" | Select-Object -ExpandProperty CounterSamples | Select-Object -ExpandProperty CookedValue" > memory_usage.txt
  fi
}

# Function to collect disk usage
collect_disk_usage() {
  if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    df -h > disk_usage.txt
  elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    powershell.exe -Command "Get-PSDrive -PSProvider FileSystem | Select-Object Name,Used,Free" > disk_usage.txt
  fi
}

# Function to collect network usage
collect_network_usage() {
  if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    netstat -i > network_usage.txt
  elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    powershell.exe -Command "Get-NetAdapter | Select-Object Name,Status,LinkSpeed" > network_usage.txt
  fi
}

# Collect data
collect_cpu_usage
collect_memory_usage
collect_disk_usage
collect_network_usage

