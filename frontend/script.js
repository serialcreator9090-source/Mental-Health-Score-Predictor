
const form = document.getElementById("prediction-form");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Convert numeric inputs from strings to numbers
    const numericFields = [
        "Age",
        "Avg_Daily_Usage_Hours",
        "Daily_Unlocks",
        "Study_Hours",
        "Physical_Activity_Hours",
        "Sleep_Hours_Per_Night"
    ];

    numericFields.forEach(field => {
        data[field] = Number(data[field]);
    });

    const output = document.getElementById("prediction-output");
    output.textContent = "Generating prediction...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(JSON.stringify(result));
        }

        output.textContent =
            "Predicted Score: " + result.predicted_mental_health_score;

    } catch (error) {
        output.textContent = "Error: " + error.message;
    }
});
