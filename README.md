<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Child Safety</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Child Safety Information</h1>
    <form id="childSafetyForm">
        <label for="childName">Child's Name:</label>
        <input type="text" id="childName" required>
        <label for="childAge">Child's Age:</label>
        <input type="number" id="childAge" required>
        <button type="submit">Get Safety Tips</button>
    </form>
    <div id="safetyTips"></div>

    <script src="script.js"></script>
</body>
</html>

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

h1 {
    text-align: center;
}

form {
    max-width: 400px;
    margin: 20px auto;
}

label,
input {
    display: block;
    margin-bottom: 10px;
}

input {
    width: 100%;
    padding: 5px;
}

button {
    padding: 8px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#safetyTips {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    display: none;
}

document.getElementById('childSafetyForm').addEventListener('submit', function(event) {
    event.preventDefault(); // prevent form submission
    var childName = document.getElementById('childName').value;
    var childAge = parseInt(document.getElementById('childAge').value);

    var safetyTips = document.getElementById('safetyTips');
    var message = "";

    if (childAge >= 0 && childAge < 3) {
        message = "For toddlers, always keep small objects out of reach and use safety gates on stairs.";
    } else if (childAge >= 3 && childAge < 6) {
        message = "For preschoolers, supervise them closely when near water and teach them to memorize important information like phone numbers.";
    } else if (childAge >= 6 && childAge < 12) {
        message = "For school-age children, educate them about stranger danger and teach them to always wear a helmet when riding a bike.";
    } else {
        message = "For teenagers, discuss online safety and set boundaries for internet and social media use.";
    }

    safetyTips.textContent = message;
    safetyTips.style.display = 'block';
});
