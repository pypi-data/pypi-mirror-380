export const listPackagesCode = `
def __mljar__list_packages():
    from importlib.metadata import distributions
    pkgs = []
    seen = set()
    for dist in distributions():
        name = dist.metadata["Name"].lower()
        if name not in seen:
            seen.add(name)
            pkgs.append({"name": name, "version": dist.version})
    return pkgs

__mljar__list_packages();
`;

export const installPackagePip = (pkg: string): string => `
def __mljar__install_pip(pkg):
    import subprocess, sys

    python_exe = sys.executable
    if python_exe.startswith('\\\\?'):
        python_exe = python_exe[4:]

    cmd = [python_exe, '-m', 'pip', 'install',
           '--progress-bar', 'off', '--no-color',
           '--disable-pip-version-check', *pkg.split()]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in iter(proc.stdout.readline, ''):
        print(line.replace('\\r', '\\n'), end='')
        sys.stdout.flush()

    proc.stdout.close()
    rc = proc.wait()
    if rc == 0:
        print('[done] Installation OK')
    else:
        print(f'[error] Installation failed:{rc}')

__mljar__install_pip('${pkg}')
`;

export const removePackagePip = (pkg: string): string => `
def __mljar__remove_package(pkg):
    import subprocess, sys

    python_exe = sys.executable
    if python_exe.startswith('\\\\?'):
        python_exe = python_exe[4:]

    cmd = [python_exe, '-m', 'pip', 'uninstall', '-y', pkg]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in iter(proc.stdout.readline, ''):
        print(line.replace('\\r', '\\n'), end='')
        sys.stdout.flush()

    proc.stdout.close()
    rc = proc.wait()
    if rc == 0:
        print('[done] Package removed')
    else:
        print(f'[error] Package removal failed:{rc}')

__mljar__remove_package('${pkg}')
`;

export const checkIfPackageInstalled = (pkg: string) => `
def __mljar__check_if_installed():
    from importlib.metadata import distributions
    from packaging import version
    import re

    m = re.match(r"^([A-Za-z0-9_\\-]+)(==|>=|<=)?([\\w\\.]+)?$", "${pkg}".strip())
    if not m:
        print("INVALID")
        return

    name, op, ver = m.groups()
    name = name.lower()

    for dist in distributions():
        if dist.metadata["Name"].lower() == name:
            if not op:
                print("INSTALLED")
                return

            dist_ver = version.parse(dist.version)
            target_ver = version.parse(ver)

            if op == "==":
                print("NOTHING_TO_CHANGE" if dist_ver == target_ver else "NOT_INSTALLED")
            elif op == ">=":
                print("NOTHING_TO_CHANGE" if dist_ver >= target_ver else "NOT_INSTALLED")
            elif op == "<=":
                print("NOTHING_TO_CHANGE" if dist_ver <= target_ver else "NOT_INSTALLED")
            return

    print("NOT_INSTALLED")

__mljar__check_if_installed()
`;

