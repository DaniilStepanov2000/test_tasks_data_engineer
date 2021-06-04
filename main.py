import math
import os
import argparse


def create_parser() -> argparse.ArgumentParser:
    """Create parser to get arguments from console

    Args:
        None.

    Returns:
        Parser object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('--user_name', default=None)
    parser.add_argument('--user_salary', default=None)

    return parser


def write_to_file(user_name: str, user_salary: str, file_name: str) -> None:
    """Add new data to file.

    Args:
        user_name: Name of user that to add to file.
        user_salary: User's salary that to add to file.
        file_name: Name of file that should open.

    Returns:
        None.
    """
    if (user_name is None) or (user_salary is None):
        return
    with open(f'data/{file_name}', 'a+') as file:
        file.write(f'{user_name} {user_salary}\n')


def check_name(name: str) -> None:
    """Check does file with this name exist.

    Args:
        name: Name of file to open.

    Returns:
        None.
    """
    if not os.path.isfile(f'data/{name}'):
        print('Sorry! The file with this name does not exist! Try again!')
        exit()


def get_line_from_file(file_name: str) -> str:
    """Get line from file.

    Args:
        file_name: Name of file to open.

    Returns:
        Line from file.
    """
    with open(f'data/{file_name}', 'r') as file:
        for line in file:
            yield line


def get_bigger_mean(all_slries: list, mean: float) -> int:
    """Finds the number of employees whose salary is higher than the mean salary.

    Args:
        all_slries: List of all employees salaries.
        mean: Mean salary.

    Returns:
        Number of employees whose salary is higher than mean salary.
    """
    count = 0

    for salary in all_slries:
        if salary > mean:
            count += 1

    return count


def get_min_max_median(all_slries: list) -> (int, int, int):
    """Find the smallest, the biggest and median salary.

    Args:
        all_slries: List of all employees salaries.

    Returns:
        Tuple that contains the smallest, the biggest and median salary.
    """
    all_slries.sort()

    if len(all_slries) % 2 == 0:
        return all_slries[len(all_slries) % 2 - 1] + all_slries[len(all_slries) % 2], min(all_slries), max(all_slries)
    return all_slries[math.ceil(len(all_slries) / 2)], min(all_slries), max(all_slries)


def get_user_slry_mean(file_name: str) -> (int, int, float, int, int):
    """Count: number of employees that in file, total employees salary, number of employees that has first letter 'K'.
       Create list of all salaries.

    Args:
        file_name: Name of file to open.

    Returns:
        Tuple that contains number of employees that in file, total employees salary, mean salary, list of all salaries,
        number of employees that has first letter 'K'.
    """
    user_count = 0
    total_slry_count = 0
    count_of_k = 0
    all_salary = []

    for line in get_line_from_file(file_name):
        data_line = line.split()
        all_salary.append(int(data_line[1]))
        if data_line[0][0] == 'k' or data_line[0][0] == 'K':
            count_of_k += 1

        total_slry_count += int(data_line[1])
        user_count += 1
    return user_count, total_slry_count, total_slry_count / user_count, all_salary, count_of_k


def print_results(number_user: int, total_salary: int,
                  mean_salary: float, median: int,
                  minimum: int, maximum: int,
                  bg_mean: int, start_k: int
                  ) -> None:
    """Print final result.

    Args:
        number_user: Number of employees in file.
        total_salary: Total salary of employees.
        mean_salary: Mean salary.
        median: Median salary.
        minimum: Minimum salary.
        maximum: Maximum salary.
        bg_mean: Number of employees whose salary is higher than mean salary.
        start_k: Number of employees that has first letter 'K'.

    Returns:
        None.
    """
    print(f'Number of users: {number_user}')
    print(f'Total salary: {total_salary}')
    print(f'Mean salary: {mean_salary}')
    print(f'Median salary: {median}')
    print(f'Minimum salary: {minimum}')
    print(f'Maximum salary: {maximum}')
    print(f'Value of users with salary bigger than mean salary: {bg_mean}')
    print(f'Number of users that name start with k: {start_k}')


def start_params(name: str) -> None:
    """Start procedure to find parameters.

    Args:
        name: name of file to read.

    Returns:
        None.
    """
    number_user, total_salary, mean_salary, salaries, start_k = get_user_slry_mean(name)
    median, minimum, maximum = get_min_max_median(salaries)
    bg_mean = get_bigger_mean(salaries, mean_salary)

    print_results(number_user, total_salary, mean_salary, median, minimum, maximum, bg_mean, start_k)


def get_arg_from_pars() -> (str, str, str):
    """Get parameters from console.

    Args:
        None.

    Returns:
        Tuple that contains name of file, employee's name, employee's salary.
    """
    parser = create_parser()
    namespace = parser.parse_args()
    name = namespace.name
    emp_name = namespace.user_name
    emp_salary = namespace.user_salary

    return name, emp_name, emp_salary


def main() -> None:
    """Start procedure.

    Args:
         None.
    Returns:
        None.
    """
    name, emp_name, emp_salary = get_arg_from_pars()

    check_name(name)
    write_to_file(emp_name, emp_salary, name)
    print('')
    start_params(name)


if __name__ == '__main__':
    main()
