function gaussSeidel(matrix, n, epsilon, initialGuesses) {
    let iteration = 1;
    let solution = initialGuesses.slice();

    while (true) {
        let prevSolution = solution.slice();

        for (let i = 0; i < n; i++) {
            let sum1 = 0;
            let sum2 = 0;

            for (let j = 0; j < i; j++) {
                sum1 += matrix[i][j] * solution[j];
            }

            for (let j = i + 1; j < n; j++) {
                sum2 += matrix[i][j] * prevSolution[j];
            }

            solution[i] = (matrix[i][n] - sum1 - sum2) / matrix[i][i];
        }

        iteration++;

        if (norm(solution, prevSolution) < epsilon) {
            console.log("Converged in", iteration, "iterations");
            return solution;
        }

        if (iteration > 1000) {
            console.log("Did not converge after 1000 iterations");
            return null;
        }
        
        // Update iteration count in the HTML
        const iterationCountElement = document.getElementById('iterationCount');
        iterationCountElement.textContent = iteration.toString();
    }
}

function norm(v1, v2) {
    let sum = 0;

    for (let i = 0; i < v1.length; i++) {
        sum += Math.pow(v1[i] - v2[i], 2);
    }

    return Math.sqrt(sum);
}

document.getElementById('calculatorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Obter os valores dos campos de entrada
    const matrixInput = document.getElementById('matrixInput').value;
    const initialGuessInput = document.getElementById('initialGuessInput').value;
    const epsilonInput = document.getElementById('epsilonInput').value;

    // Converter a entrada da matriz em um array de arrays
    const matrixRows = matrixInput.trim().split('\n');
    const matrix = matrixRows.map(row => row.split(' ').map(Number));

    // Converter a entrada do chute inicial em um array de números
    const initialGuesses = initialGuessInput.trim().split(' ').map(Number);

    // Converter o valor do epsilon para um número
    const epsilon = parseFloat(epsilonInput);

    // Calcular Gauss-Seidel
    const result = gaussSeidel(matrix, matrix.length, epsilon, initialGuesses);

    // Exibir o resultado no HTML
    const finalValueElement = document.getElementById('finalValue');
    const convergenceStatusElement = document.getElementById('convergenceStatus');
    const iterationCountElement = document.getElementById('iterationCount');

    if (result !== null) {
        finalValueElement.textContent = result.join(', ');
        convergenceStatusElement.textContent = 'Sim';
    } else {
        finalValueElement.textContent = '';
        convergenceStatusElement.textContent = 'Não';
    }
});

