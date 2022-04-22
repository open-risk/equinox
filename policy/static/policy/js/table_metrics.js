    //
    // DATATABLE OF METRICS
    //

    var dictionary = {
        "Max" : ["Maximum Value", "The maximum value observed for the timeseries, at any time"],
        "Q75" : ["75% Percentile", "One in four observations is above this threshold"],
        "Median" : ["Median Value", "Half of the observations are above (below) this threshold"],
        "Q25" : ["25% Percentile", "One in four observations is below this threshold"],
        "Min" : ["Minimum Value", "The minimum value observed for the timeseries, at any time"],
        "Vol" : ["Volatility", "The standard deviation calculated using the entire timeseries"],
        "Mean" : ["Mean Value", "The average observation calculated using the entire timeseries"],
        "ObsCount" : ["No of Observations", "The total number of valid observations"],
        "FirstDate" : ["Earliest Measurement", "The first available observation"],
        "LastDate" : ["Latest Measurement", "The latest (most recent) available observation"],
        "Frequency" : ["Measurement Frequency", "The time interval between successive observations"],
        "Skew" : ["Skew", "The third moment of the distribution calculated using all observations"],
        "Kurtosis" : ["Kurtosis","The fourth moment of the distribution calculated using all observations"]
    }

    var metricSet = [];
    for (var key in dictionary) {
        var dataEntry = [dictionary[key][0], metrics[key], dictionary[key][1]];
        metricSet.push(dataEntry);
    }
    metricSet.push(["Measurement Unit", units, "The unit of measurement (or percentage)"]);


    table2 = $('#metrics').DataTable( {
    data: metricSet,
    "bPaginate": false,
    "responsive": true,
    "bSort" : false,
    "ordering": false,
    "info":     false,
    "searching": false,
    "pageLength": -1,
    columns: [
        { width: "25%", title: "Risk Metrics" },
        { width: "15%", title: "Values" },
        { width: "60%", title: "Description" },
            ]
    } );




