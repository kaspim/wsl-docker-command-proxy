import sys, subprocess

if __name__ == '__main__':
    arguments = sys.argv

    # Remove the first argument (the script name)
    if len(arguments) > 0:
        del arguments[0]

    # Base command to run Docker in WSL
    command = ['wsl.exe', '-d', 'Ubuntu', 'docker']

    try:
        proc = subprocess.Popen(command + arguments, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout.decode('utf-8'))
    except KeyboardInterrupt:
        proc.terminate()
