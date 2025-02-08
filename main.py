import os

def make_commit(days: int):
    if days < 1:
        # Push to GitHub
        os.system('git push')
        return
    
    dates = f'{days} days ago'

    with open('data.txt', 'a') as file:
        file.write(f'{dates}\n')

    # Staging and committing
    os.system('git add data.txt')
    os.system(f'git commit --date="{dates}" -m "Commit for {dates}"')

    # Recursive call without returning the function
    make_commit(days - 1)

# Run the function
make_commit(365)
