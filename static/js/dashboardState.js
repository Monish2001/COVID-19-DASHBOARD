function specificState() {
    var fromDate = document.getElementById("fromDate").value;
    var toDate = document.getElementById("toDate").value;

    var entry = {
        fromDate: fromDate,
        toDate: toDate
    };

    var dropDown = document.getElementById("mySelect").value;

    //USING ARROW FUNCTION

    fetch('/api/v1/states/' + dropDown, {
            method: "POST",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then((res) => res.text())
        .then((data) => {
            document.getElementById("resultArea").innerHTML = data;
        })
        .catch((err) => console.log(err))
}


function dropDownList() {

    fetch('/api/v1/statelist', { method: 'GET' })
        .then((res) => res.json())
        .then((data) => {

            var dropBox = document.getElementById("mySelect");
            for (var i = 0; i < data.length; i++) {
                dropBox.options.add(new Option(data[i]));

            }
        })
}

dropDownList();