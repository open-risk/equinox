    //
    // DATATABLE TIMESERIES
    //

    var dataSet = [];
    for(i = 0; i<dates.length; i++){
        var dataEntry = [dates[i], values[i], Math.round(values_diff[i] * 1000) / 1000, Math.round(values_diff_p[i] * 1000) / 10];
        dataSet.push(dataEntry);
    }

    table1 = $('#dataseries').DataTable( {
    data: dataSet,
    pagingType: "full_numbers",
    "iDisplayLength": 25,
    "responsive": true,
    "info":     false,
    "searching": false,
    "order": [[ 0, "desc" ]],
    "columnDefs": [
        { className: "dt-center", "targets": [ 0, 1, 2, 3 ] }
    ],
    columns: [
        { width: "25%", title: "Observation Date" },
        { width: "25%", title: "Value" },
        { width: "25%", title: "Change Delta (Absolute)" },
        { width: "25%", title: "Change Delta (%)" }
            ]
    } );

    var data = table1.column(1).data();
    table1.column(1).nodes().each( function (cell, i) {
        if ( data[i] < data[i+1] ) {
            $(cell).css('color', 'red');
        }
        else {
            $(cell).css('color', 'green');
        }
    });
    table1.column(2).nodes().each( function (cell, i) {
        if ( data[i] < data[i+1] ) {
            $(cell).css('color', 'red');
        }
        else {
            $(cell).css('color', 'green');
        }
    });
    table1.column(3).nodes().each( function (cell, i) {
        if ( data[i] < data[i+1] ) {
            $(cell).css('color', 'red');
        }
        else {
            $(cell).css('color', 'green');
        }
    });
