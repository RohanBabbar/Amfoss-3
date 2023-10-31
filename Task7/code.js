const apiKey = "d7763b0e1dbbe31ba811b01863a5ccb4";
const apiURL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");

async function weatherUpdate(city) {
    const response = await fetch(apiURL + city + `&appid=${apiKey}`);
    const data = await response.json();

    if(response.status == 404){
        document.querySelector(".error").style.display = "block"
        document.querySelector(".weather").style.display = "none"

    }else{
        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        // document.querySelector(".humidity").innerHTML = data.main.humidity;
        // document.querySelector(".wind").innerHTML = data.wind.speed;
    
        if (data.weather[0].main == "Clouds") {
            weatherIcon.src = "img/images/clouds.png";
        } else if (data.weather[0].main == "Clear") {
            weatherIcon.src = "img/images/clear.png";
        } else if (data.weather[0].main == "Rain") {
            weatherIcon.src = "img/images/rain.png";
        } else if (data.weather[0].main == "Drizzle") {
            weatherIcon.src = "img/images/drizzle.png";
        } else if (data.weather[0].main == "Mist") {
            weatherIcon.src = "img/images/mist.png";
        }
    
        document.querySelector(".weather").style.display = "block";
    } 
    }

   

searchBtn.addEventListener("click", () => {
    weatherUpdate(searchBox.value);
});
searchBox.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        weatherUpdate(searchBox.value);
    }
});
