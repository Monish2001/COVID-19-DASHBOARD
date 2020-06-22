function stateTable() {

    var fromDate = document.getElementById("fromDate").value;
    var toDate = document.getElementById("toDate").value;

    var entry = {
        fromDate: fromDate,
        toDate: toDate
    };

    fetch('/api/v1/states', {
            method: "POST",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then((res) => res.json())
        .then((data) => {

            var table = '';
            for (var r = 0; r < data.length; r++) {
                table += '<tr>';
                table += '<td>' + (r + 1) + '</td>';

                for (var c = 0; c < data[r].length; c++) {
                    table += '<td>' + data[r][c] + '</td>';
                }
                table += '</tr>';
            }

            document.getElementById("resultArea").innerHTML = ('<table class="table table-striped table-dark">' + '<thead><tr><th scope="col">S.NO</th><th scope="col">STATE</th><th scope="col">CHANGE IN CASE</th></tr>' + table + '</table>');

        })

}