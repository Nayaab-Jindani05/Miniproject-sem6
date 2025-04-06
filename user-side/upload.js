function uploadResume() {
    let fileInput = document.getElementById("resumeFile");
    if (fileInput.files.length === 0) {
        document.getElementById("message").innerText = "Please select a file!";
        return;
    }

    let formData = new FormData();
    formData.append("resume", fileInput.files[0]);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}
