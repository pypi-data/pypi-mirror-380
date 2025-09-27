document.addEventListener('DOMContentLoaded', () => {
    const benchmarkList = document.getElementById('benchmark-list');
    const saveBtn = document.getElementById('save-benchmark-btn');
    const newBtn = document.getElementById('new-benchmark-btn');
    const deleteBtn = document.getElementById('delete-benchmark-btn');
    const addPromptBtn = document.getElementById('add-prompt-btn');
    const promptsList = document.getElementById('prompts-list');

    const form = {
        name: document.getElementById('benchmark-name'),
        description: document.getElementById('benchmark-desc'),
        author: document.getElementById('author'),
        revision: document.getElementById('revision'),
        systemPrompt: document.getElementById('system-prompt'),
        currentFilename: document.getElementById('current-filename'),
        formTitle: document.getElementById('form-title'),
        evaluationType: document.getElementById('evaluation-type'),
    };

    // --- Utility Functions ---
    const showToast = (message, isError = false) => {
        const toast = document.getElementById('toast');
        const toastMessage = document.getElementById('toast-message');
        toastMessage.textContent = message;
        toast.className = `fixed bottom-5 right-5 text-white py-2 px-4 rounded-lg shadow-lg transition-opacity duration-300 opacity-100 ${isError ? 'bg-red-600' : 'bg-green-600'}`;
        setTimeout(() => {
            toast.style.opacity = '0';
        }, 3000);
    };

    // --- API Calls ---
    const api = {
        getBenchmarks: async () => {
            const response = await fetch('/api/benchmarks');
            if (!response.ok) throw new Error('Failed to fetch benchmarks.');
            return response.json();
        },
        getBenchmark: async (filename) => {
            const response = await fetch(`/api/benchmarks/${filename}`);
            if (!response.ok) throw new Error('Failed to load benchmark.');
            return response.json();
        },
        saveBenchmark: async (data) => {
            const response = await fetch('/api/benchmarks', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to save benchmark.');
            }
            return response.json();
        },
        deleteBenchmark: async (filename) => {
            const response = await fetch(`/api/benchmarks/${filename}`, { method: 'DELETE' });
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to delete benchmark.');
            }
            return response.json();
        }
    };

    // --- UI Rendering ---
    const renderBenchmarkList = async () => {
        try {
            const benchmarks = await api.getBenchmarks();
            benchmarkList.innerHTML = '';
            benchmarks.sort((a, b) => a.name.localeCompare(b.name));
            benchmarks.forEach(bench => {
                const item = document.createElement('a');
                item.href = '#';
                item.textContent = bench.name;
                item.dataset.filename = bench.filename;
                item.className = 'block py-2 px-3 rounded-lg sidebar-item transition duration-200';
                benchmarkList.appendChild(item);
            });
            updateActiveSidebarItem();
        } catch (error) {
            showToast(error.message, true);
        }
    };

    const createPromptElement = (input = '', target = '', metadata = {}) => {
        const div = document.createElement('div');
        div.className = 'p-4 bg-gray-700 rounded-lg prompt-pair';
        div.innerHTML = `
            <div class="flex justify-between items-center mb-2">
                <h4 class="font-semibold text-gray-300">Sample</h4>
                <button class="remove-prompt-btn text-red-400 hover:text-red-500 font-bold text-sm">Remove</button>
            </div>
            <div class="space-y-2">
                <textarea rows="3" placeholder="Input / Prompt" class="sample-input w-full bg-gray-600 rounded-md p-2 text-sm">${input}</textarea>
                <textarea rows="3" placeholder="Target / Ideal Answer" class="sample-target w-full bg-gray-600 rounded-md p-2 text-sm">${target}</textarea>
                
                <div class="metadata-section bg-gray-800 p-2 rounded-md">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-gray-300 text-sm font-semibold">Metadata</span>
                        <button class="add-metadata-btn text-indigo-400 hover:text-indigo-500 text-sm">+ Add</button>
                    </div>
                    <div class="metadata-list space-y-2"></div>
                </div>
            </div>
        `;

        const metadataList = div.querySelector('.metadata-list');
        const addBtn = div.querySelector('.add-metadata-btn');

        const addMetadataRow = (key = '', value = '') => {
            const row = document.createElement('div');
            row.className = 'flex space-x-2 items-center';
            row.innerHTML = `
                <input type="text" value="${key}" placeholder="Key" class="meta-key flex-1 bg-gray-600 rounded-md p-2 text-sm">
                <input type="text" value="${value}" placeholder="Value" class="meta-value flex-1 bg-gray-600 rounded-md p-2 text-sm">
                <button class="remove-meta-btn text-red-400 hover:text-red-500 font-bold text-xs">✕</button>
            `;
            metadataList.appendChild(row);

            row.querySelector('.remove-meta-btn').addEventListener('click', () => row.remove());
        };

        addBtn.addEventListener('click', (e) => {
            e.preventDefault();
            addMetadataRow();
        });

        // preload metadata if any
        if (metadata && typeof metadata === 'object') {
            Object.entries(metadata).forEach(([k, v]) => addMetadataRow(k, v));
        }

        promptsList.appendChild(div);
    };

    const populateForm = (data) => {
        form.name.value = data.name || '';
        form.description.value = data.description || '';
        form.author.value = data.author || '';
        form.revision.value = data.revision || '';
        form.systemPrompt.value = data.systemPrompt || '';
        form.evaluationType.value = data.evaluationType || 'multiple_choice';

        // Clear and rebuild sample fields
        promptsList.innerHTML = '';
        if (data.samples) {
            data.samples.forEach(s => {
                createPromptElement(
                    s.input || '',
                    s.target || '',
                    s.metadata || {}
                );
            });
        } else {
            createPromptElement();
        }

        form.formTitle.textContent = `Editing: ${data.name}`;
        deleteBtn.classList.remove('hidden');
    };

    const clearForm = () => {
        form.name.value = '';
        form.description.value = '';
        form.author.value = '';
        form.revision.value = '';
        form.systemPrompt.value = '';
        promptsList.innerHTML = '';
        createPromptElement(); // Add one empty prompt
        form.currentFilename.value = '';
        form.formTitle.textContent = 'New Evaluation';
        deleteBtn.classList.add('hidden');
        updateActiveSidebarItem();
    };

    const updateActiveSidebarItem = () => {
        const currentFile = form.currentFilename.value;
        document.querySelectorAll('#benchmark-list .sidebar-item').forEach(item => {
            if (item.dataset.filename === currentFile) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    };

    // --- Event Handlers ---
    const handleLoadBenchmark = async (filename) => {
        try {
            const data = await api.getBenchmark(filename);
            form.currentFilename.value = filename;
            populateForm(data);
            updateActiveSidebarItem();
        } catch (error) {
            showToast(error.message, true);
        }
    };

    const handleSaveBenchmark = async () => {
        const samples = Array.from(document.querySelectorAll('.prompt-pair')).map((div, i) => {
            const input = div.querySelector('.sample-input').value;
            const target = div.querySelector('.sample-target').value;

            // Collect metadata rows
            const metadataRows = div.querySelectorAll('.metadata-list .flex');
            let metadata = {};
            metadataRows.forEach(row => {
                const key = row.querySelector('.meta-key').value.trim();
                const value = row.querySelector('.meta-value').value.trim();
                if (key) metadata[key] = value;
            });
            if (Object.keys(metadata).length === 0) metadata = null;

            return {
                id: i + 1,
                input,
                target,
                metadata,
                files: null,
                setup: null
            };
        });

        if (!form.name.value.trim()) {
            showToast("Evaluation Name cannot be empty.", true);
            return;
        }

        const data = {
            name: form.name.value,
            description: form.description.value,
            author: form.author.value,
            revision: form.revision.value,
            evaluationType: form.evaluationType.value,
            systemPrompt: form.systemPrompt.value,
            samples
        };

        try {
            const result = await api.saveBenchmark(data);
            form.currentFilename.value = result.filename;
            showToast(result.message);
            await renderBenchmarkList();
            form.formTitle.textContent = `Editing: ${data.name}`;
            deleteBtn.classList.remove('hidden');
        } catch (error) {
            showToast(error.message, true);
        }
    };


    const handleDeleteBenchmark = async () => {
        const filename = form.currentFilename.value;
        if (!filename || !confirm(`Are you sure you want to delete this benchmark?`)) return;

        try {
            const result = await api.deleteBenchmark(filename);
            showToast(result.message);
            clearForm();
            await renderBenchmarkList();
        } catch (error) {
            showToast(error.message, true);
        }
    };

    // --- Event Listeners Setup ---
    benchmarkList.addEventListener('click', (e) => {
        if (e.target.matches('.sidebar-item')) {
            e.preventDefault();
            const filename = e.target.dataset.filename;
            handleLoadBenchmark(filename);
        }
    });

    promptsList.addEventListener('click', (e) => {
        if (e.target.matches('.remove-prompt-btn')) {
            e.target.closest('.prompt-pair').remove();
        }
    });

    saveBtn.addEventListener('click', handleSaveBenchmark);
    newBtn.addEventListener('click', clearForm);

    deleteBtn.addEventListener('click', handleDeleteBenchmark);
    addPromptBtn.addEventListener('click', () => createPromptElement());

    // --- Initial Load ---
    const initialize = async () => {
        await renderBenchmarkList();
        clearForm();
    };

    initialize();
});
