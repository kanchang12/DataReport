// Function to handle file upload and process the CSV data
function handleFileUpload() {
    const fileInput = document.getElementById('csvFile');
    const userInput = document.getElementById('userInput').value;

    // Check if a file is selected
    if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
        alert('Please select a CSV file.');
        return;
    }

    // Retrieve the uploaded file
    const file = fileInput.files[0];

    // Validate file type (must be CSV)
    if (!file.name.endsWith('.csv')) {
        alert('Please upload a CSV file.');
        return;
    }

    // Read the contents of the CSV file
    const reader = new FileReader();
    reader.onload = function (event) {
        const csvData = event.target.result;
        // Process the CSV data and display result
        displayResult(csvData, userInput);
    };
    reader.readAsText(file);
}

// Function to display the processed result
function displayResult(csvData, userInput) {
    // Example: Process CSV data and generate report content
    const reportContent = `<h2>Analysis Report</h2>
                          <p>User Input: ${userInput}</p>
                          <p>CSV Data:</p>
                          <pre>${csvData}</pre>`;

    // Display the report content in the result preview area
    const reportPreview = document.getElementById('reportPreview');
    reportPreview.innerHTML = reportContent;
}

// Function to trigger the report download
function downloadReport() {
    const reportContent = document.getElementById('reportPreview').innerHTML;
    const fileName = 'analysis_report.html'; // Name for the downloaded file
    const blob = new Blob([reportContent], { type: 'text/html' });

    // Create a temporary link element to trigger the download
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = fileName;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}


function downloadReport() {
    const reportContent = document.getElementById('reportPreview').innerHTML;

    // Create new jsPDF instance
    const doc = new jsPDF();

    // Add HTML content to PDF
    doc.html(reportContent, {
        callback: function (doc) {
            // Save PDF as file
            doc.save('analysis_report.pdf');
        },
        x: 10,
        y: 10
    });
}

function downloadReport() {
    const reportContent = document.getElementById('reportPreview').innerHTML;

    // Convert HTML to Word document
    const docx = HTMLDocX.asBlob(reportContent);

    // Create temporary link element to trigger download
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(docx);
    downloadLink.download = 'analysis_report.docx';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}
