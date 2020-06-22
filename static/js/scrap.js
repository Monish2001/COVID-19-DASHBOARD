function scrap() {

    //USING ARROW FUNCTION

    fetch('/api/v1/scrap', { method: 'GET' })
        .then((res) => res.text())
        .then((data) => {
            document.getElementById("resultArea").innerHTML = data;
        })
        .catch((err) => console.log(err))

}

function refresh() {
    window.onload = startInterval;

    function startInterval() {
        setInterval("scrap();", 3600000);
    }
}
refresh();