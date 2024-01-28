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
