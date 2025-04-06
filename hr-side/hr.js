document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:5000/resumes")
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById("resumeList");
            data.forEach(resume => {
                let li = document.createElement("li");
                li.textContent = resume.filename;
                list.appendChild(li);
            });
        })
        .catch(error => console.error("Error:", error));
});
