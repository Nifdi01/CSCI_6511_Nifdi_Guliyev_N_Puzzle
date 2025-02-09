from utils.read_puzzle import read_puzzle

def main():
    file_path = 'n-puzzle.txt'
    try:
        initial_state = read_puzzle(file_path)
        print(initial_state)
    except Exception as e:
        print(f"Error reading puzzle file: {e}")
        return
    
    
if __name__ == '__main__':
    main()