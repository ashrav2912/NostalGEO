

async function getCurrentPosition() {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            position => resolve(position),
            error => reject(error)
        );
    });
}

async function initMap() {
    try {
        const position = await getCurrentPosition();
        const { latitude, longitude } = position.coords;

        const map = L.map('map').setView([latitude, longitude], 13);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        const you = L.marker([latitude, longitude]).addTo(map);

        // Now that the map is initialized, make the fetch request
        fetch('http://localhost:3000/get_markers')
            .then(response => response.json())
            .then(data => {
                data.forEach(marker => {
                    console.log(marker);
                    L.marker([marker.lat, marker.long]).addTo(map);
                });
            })
            .catch(error => {
                console.error('Error fetching markers:', error.message);
            });
    } catch (error) {
        console.error('Error getting geolocation:', error.message);
    }
}

// Call the function to initialize the map
initMap();

// Create button click event handler
const createButton = document.getElementById('create');
const fileUpload = document.getElementById('fileupload');
createButton.addEventListener('click', () => {fileUpload.click();})
fileUpload.addEventListener('change', async (event) => {
    const files = event.target.files;
    // Handle the uploaded file here
    console.log('Uploaded file:', files);

    // Save each file to the "assets" folder with a unique name
    const formData = new FormData();
    Array.from(files).forEach((file) => {
        formData.append('file', file);


        // const uniqueName = generateUniqueName(file.name);
        // const filePath = path.join(__dirname, 'assets', uniqueName);

        // fs.writeFile(filePath, file, (err) => {
        //     if (err) {
        //         console.error('Error saving file:', err);
        //     } else {
        //         console.log('File saved:', filePath);
        //         // Save the file path to the database
        //         saveFilePathToDatabase(filePath);
        //     }
        // });
    });

    // create new time capsule and shit
    let time_capsule_id
    let currPos = await getCurrentPosition();
    fetch('http://localhost:3000/create_time_capsule?lat=' + currPos.coords.latitude + '&long=' + currPos.coords.longitude + '&date=' + Date.now())
    .then((response) => {
        time_capsule_id = response._id;
    })

    // SEND FILES TO BACKEND
    const response = await fetch('http://localhost:3000/upload?time_capsule_id=' + time_capsule_id, {
        method: 'POST',
        body: formData
    });
    if (response.ok) {
        console.log('Files uploaded successfully');
    } else {
        console.error('Error uploading files:', response.status, response.statusText);
    }
});

function generateUniqueName(originalName) {
    const timestamp = Date.now();
    const randomString = Math.random().toString(36).substring(2, 8);
    return `${timestamp}_${randomString}`;
}

function saveFilePathToDatabase(filePath) {
    // Implement your code to save the file path to the database here
    console.log('File path saved to database:', filePath);
}


