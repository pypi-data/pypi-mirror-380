document.addEventListener('DOMContentLoaded', () => {
    const benchmarkSelect = document.getElementById('benchmark-select');
    const modelSelect = document.getElementById('model-select');
    const runEvalBtn = document.getElementById('run-eval-btn');
    const resultsTableBody = document.getElementById('results-table-body');
    const refreshBtn = document.getElementById('refresh-results-btn');
    const graphBenchmarkSelect = document.getElementById('graph-benchmark-select');
    const toast = document.getElementById('toast');

    let resultsChart = null;
    let allResults = [];

    const showToast = (message, isError = false) => {
        toast.textContent = message;
        toast.className = `fixed bottom-5 right-5 text-white py-2 px-4 rounded-lg shadow-lg transition-opacity duration-300 opacity-100 ${isError ? 'bg-red-600' : 'bg-green-600'}`;
        setTimeout(() => { toast.style.opacity = '0'; }, 3000);
    };

    const populateSelect = async (selectElement, url, valueField, nameField) => {
        try {
            const response = await fetch(url);
            const data = await response.json();
            selectElement.innerHTML = '';
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item[valueField];
                option.textContent = item[nameField];
                selectElement.appendChild(option);
            });
            return data;
        } catch (error) {
            showToast('Failed to load data for dropdowns.', true);
        }
    };

    const renderResultsTable = (results) => {
        resultsTableBody.innerHTML = '';
        results.forEach(res => {
            const row = document.createElement('tr');
            row.className = 'border-b border-gray-700 hover:bg-gray-700';
            row.innerHTML = `
                <td class="py-2 px-4">${new Date(res.timestamp).toLocaleString()}</td>
                <td class="py-2 px-4">${res.benchmark_name}</td>
                <td class="py-2 px-4">${res.model}</td>
                <td class="py-2 px-4 font-mono">${res.accuracy.toFixed(2)}%</td>
            `;
            resultsTableBody.appendChild(row);
        });
    };

    const renderChart = () => {
        const selectedBenchmark = graphBenchmarkSelect.value;
        if (!selectedBenchmark) return;

        const filteredData = allResults.filter(r => r.benchmark_name === selectedBenchmark);

        const chartData = {
            labels: filteredData.map(r => r.model),
            datasets: [{
                label: `Accuracy for ${selectedBenchmark}`,
                data: filteredData.map(r => r.accuracy),
                backgroundColor: 'rgba(79, 70, 229, 0.8)',
                borderColor: 'rgba(99, 102, 241, 1)',
                borderWidth: 1
            }]
        };

        const ctx = document.getElementById('resultsChart').getContext('2d');
        if (resultsChart) {
            resultsChart.destroy();
        }
        resultsChart = new Chart(ctx, {
            type: 'bar',
            data: chartData,
            options: {
                scales: {
                    y: { beginAtZero: true, max: 100 }
                }
            }
        });
    };

    const loadResults = async () => {
        try {
            const response = await fetch('/run/results');
            allResults = await response.json();
            renderResultsTable(allResults);

            const uniqueBenchmarks = [...new Set(allResults.map(r => r.benchmark_name))];
            graphBenchmarkSelect.innerHTML = uniqueBenchmarks.map(name => `<option value="${name}">${name}</option>`).join('');
            if (uniqueBenchmarks.length > 0) {
                graphBenchmarkSelect.value = uniqueBenchmarks[0];
                renderChart();
            }
        } catch (error) {
            showToast('Failed to load results.', true);
        }
    };

    runEvalBtn.addEventListener('click', async () => {
        const benchmark_file = benchmarkSelect.value;
        const model_name = modelSelect.value;
        if (!benchmark_file || !model_name) {
            showToast('Please select both a benchmark and a model.', true);
            return;
        }

        try {
            runEvalBtn.disabled = true;
            runEvalBtn.textContent = 'Running...';
            const response = await fetch('/run/benchmark', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ benchmark_file, model_name })
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.error);
            showToast(result.message);
        } catch (error) {
            showToast(error.message, true);
        } finally {
            runEvalBtn.disabled = false;
            runEvalBtn.textContent = 'Run Eval';
        }
    });

    refreshBtn.addEventListener('click', loadResults);
    graphBenchmarkSelect.addEventListener('change', renderChart);

    const initialize = async () => {
        populateSelect(benchmarkSelect, '/api/benchmarks', 'filename', 'name');
        populateSelect(modelSelect, '/run/models', 'id', 'name');
        await loadResults();
    };

    initialize();
});
