document.addEventListener('DOMContentLoaded', () => {
    const benchmarkSelect = document.getElementById('benchmark-select');
    const modelSelector = document.getElementById('model-selector');
    const chartCanvas = document.getElementById('topic-spider-chart');
    let spiderChart = null;
    let allResults = [];

    // Set default chart font color
    Chart.defaults.color = '#e5e7eb';

    const backgroundColors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(199, 199, 199, 0.2)'
    ];
    const borderColors = [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(199, 199, 199, 1)'
    ];

    const showToast = (message, isError = false) => {
        const toast = document.getElementById('toast');
        toast.textContent = message;
        toast.className = `fixed bottom-5 right-5 text-white py-2 px-4 rounded-lg shadow-lg transition-opacity duration-300 opacity-100 ${isError ? 'bg-red-600' : 'bg-green-600'}`;
        setTimeout(() => { toast.style.opacity = '0'; }, 3000);
    };

    const populateBenchmarkSelect = () => {
        const benchmarkNames = [...new Set(allResults.map(r => r.benchmark_name))];
        benchmarkSelect.innerHTML = '';
        benchmarkNames.forEach(name => {
            const option = document.createElement('option');
            option.value = name;
            option.textContent = name;
            benchmarkSelect.appendChild(option);
        });
        if (benchmarkNames.length > 0) {
            populateModelSelector(benchmarkNames[0]);
        }
    };

    const populateModelSelector = (benchmarkName) => {
        const models = [...new Set(allResults.filter(r => r.benchmark_name === benchmarkName).map(r => r.model))];
        modelSelector.innerHTML = '';
        models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            option.selected = true;
            modelSelector.appendChild(option);
        });
        updateChart();
    };

    const updateChart = () => {
        const selectedBenchmark = benchmarkSelect.value;
        const selectedModels = Array.from(modelSelector.selectedOptions).map(option => option.value);

        if (spiderChart) {
            spiderChart.destroy();
        }

        const benchmarkResults = allResults.filter(r => r.benchmark_name === selectedBenchmark);
        const allTopics = [...new Set(benchmarkResults.flatMap(r => r.details.map(d => d.topic)))];

        const datasets = selectedModels.map((model, index) => {
            const result = benchmarkResults.find(r => r.model === model);
            const topicResults = {};

            if (result) {
                result.details.forEach(detail => {
                    if (!topicResults[detail.topic]) {
                        topicResults[detail.topic] = { correct: 0, total: 0 };
                    }
                    topicResults[detail.topic].total++;
                    if (detail.is_correct) {
                        topicResults[detail.topic].correct++;
                    }
                });
            }

            const data = allTopics.map(topic => {
                if (topicResults[topic]) {
                    return (topicResults[topic].correct / topicResults[topic].total) * 100;
                }
                return 0;
            });

            return {
                label: model,
                data: data,
                backgroundColor: backgroundColors[index % backgroundColors.length],
                borderColor: borderColors[index % borderColors.length],
                pointBackgroundColor: borderColors[index % borderColors.length],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: borderColors[index % borderColors.length],
                borderWidth: 1
            };
        });

        spiderChart = new Chart(chartCanvas, {
            type: 'radar',
            data: {
                labels: allTopics,
                datasets: datasets
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: {
                            display: true,
                            color: 'rgba(255, 255, 255, 0.2)'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.2)'
                        },
                        pointLabels: {
                            font: {
                                size: 12
                            },
                            color: '#e5e7eb'
                        },
                        ticks: {
                            display: false
                        },
                        suggestedMin: 0,
                        suggestedMax: 100
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: `Model Performance for ${selectedBenchmark}`,
                        font: {
                            size: 18
                        }
                    },
                    legend: {
                        labels: {
                            font: {
                                size: 14
                            }
                        }
                    }
                }
            }
        });
    };

    benchmarkSelect.addEventListener('change', (event) => {
        populateModelSelector(event.target.value);
    });
    modelSelector.addEventListener('change', updateChart);

    const initialize = async () => {
        try {
            const response = await fetch('/review/results');
            allResults = await response.json();
            populateBenchmarkSelect();
        } catch (error) {
            showToast('Failed to load results.', true);
        }
    };

    initialize();
});