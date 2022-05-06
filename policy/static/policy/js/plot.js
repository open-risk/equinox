// SELECT TIMESERIES GRAPH

if (datatype == 'numerical') {
    timeseries_graph_numerical(title, dates, values, metrics);
    console.log('Numerical')
} else {
    timeseries_graph_ordinal(title, dates, values, metrics);
    console.log('Ordinal')
}

