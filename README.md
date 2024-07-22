# Python Challenge

This repository contains two Python projects: `PyBank` and `PyPoll`.

## PyBank

### Overview

The `PyBank` project analyzes financial records from a CSV file to provide insights such as:
- Total number of months
- Net total amount of profit/losses
- Average change in profit/losses
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)

### Project Structure

- `Resources/budget_data.csv`: Contains the financial data.
- `main.py`: Reads the financial data, performs calculations, and outputs the results.
- `analysis`: Directory where the output results are saved as a text file.

### How It Works

1. **Reading the CSV File**: 
   - The script uses the `csv` module to read the data.
   - The file path is defined using `os.path.join`.

2. **Initializing Variables**:
   - Variables are initialized to store total months, net total amount, changes, previous profit, greatest increase, and greatest decrease.

3. **Processing Each Row**:
   - Iterates through each row, updating total months and net total.
   - Calculates the change in profit/losses and stores it.

4. **Calculating Results**:
   - Calculates average change.
   - Identifies the greatest increase and decrease in profits.

5. **Outputting Results**:
   - Prints results to the terminal and saves them to a text file in the `analysis` directory.

## PyPoll

### Overview

The `PyPoll` project analyzes election data from a CSV file to provide insights such as:
- Total number of votes
- Total and percentage of votes for each candidate
- Winner of the election

### Project Structure

- `Resources/election_data.csv`: Contains the election data.
- `main.py`: Reads the election data, performs calculations, and outputs the results.
- `analysis`: Directory where the output results are saved as a text file.

### How It Works

1. **Reading the CSV File**:
   - The script uses the `csv` module to read the data.
   - The file path is defined using `os.path.join`.

2. **Initializing Variables**:
   - Variables are initialized to store total votes, candidates' vote counts, and the winner.

3. **Processing Each Row**:
   - Iterates through each row, updating total votes and counting votes for each candidate.

4. **Calculating Results**:
   - Calculates the percentage of votes each candidate received.
   - Determines the winner based on the highest vote count.

5. **Outputting Results**:
   - Prints results to the terminal and saves them to a text file in the `analysis` directory.
.

## Code Source

This project includes code inspired by class activities, explanations provided by the instructor in class, and resources such as Stack Overflow. The structure and logic are influenced by these sources to provide a comprehensive analysis.
