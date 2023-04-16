def electron_shell(electrons):
    shell_distribution = []
    shell = 1
    while electrons > 0:
        electrons_in_shell = 2 * pow(shell, 2)
        shell_distribution.append(electrons_in_shell if electrons > electrons_in_shell else electrons)
        electrons -= electrons_in_shell
        shell += 1
    return shell_distribution


print(electron_shell(int(input())))
