// Function to handle file upload and process the CSV data
function handleFileUpload(event) {
    event.preventDefault(); // Prevent default form submission behavior

    const fileInput = document.getElementById('csvFile');
    const userInput = document.getElementById('userInput').value;

    // Check if a file is selected
    if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
        alert('Please select a CSV file.');
        return false;
    }

    // Retrieve the uploaded file
    const file = fileInput.files[0];

    // Validate file type (must be CSV)
    if (!file.name.endsWith('.csv')) {
        alert('Please upload a CSV file.');
        return false;
    }

    // Read the contents of the CSV file
    const reader = new FileReader();
    reader.onload = function (event) {
        const csvData = event.target.result;
        // Process the CSV data (simulated processing delay)
        setTimeout(() => {
            // After processing, redirect to analysis.html
            window.location.href = `analysis.html?userInput=${encodeURIComponent(userInput)}`;
        }, 2000); // Simulated processing delay (2 seconds)
    };
    reader.readAsText(file);

    return false; // Prevent form submission
}
