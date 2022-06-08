function timeseries_graph(dates, values) {

    // d3.select("#timeseries_values").html("");

    var value_grid = d3.select("#timeseries_values")
        .selectAll("li")
        .data(values)
        .enter()
        .append("li")
        .attr("id", function (d, i) {
            return "v" + i.toString()
        })
        .text(function (d) {
            return d;
        });

    d3.select("#timeseries_graph").html("");

    var graph_object = {};

    var max_val = Math.max.apply(Math, values);
    var min_val = Math.min.apply(Math, values);

    var max_date = Math.max.apply(Math, dates);
    var min_date = Math.min.apply(Math, dates);

    var data = [];
    for (var k = 0; k < dates.length; k++) {
        data.push({'date': dates[k], 'value': values[k]})
    }


    graph_object.margin = {top: 20, right: 50, bottom: 50, left: 50};
    graph_object.width = 750 - graph_object.margin.left - graph_object.margin.right;
    graph_object.height = 400 - graph_object.margin.top - graph_object.margin.bottom;

    graph_object.xScale = d3.scale.linear()
        .domain([min_date, max_date])
        .range([0, graph_object.width]);

    graph_object.yScale = d3.scale.linear()
        .domain([0.95 * min_val, 1.05 * max_val])
        .range([graph_object.height, 0]);

    graph_object.xAxis = d3.svg.axis()
        .scale(graph_object.xScale)
        .innerTickSize(-graph_object.height)
        .outerTickSize(0)
        .tickPadding(10)
        .orient("bottom");

    xlabel_y = 40;
    xlabel_x = graph_object.width / 2 + 20;

    graph_object.yAxisL = d3.svg.axis()
        .scale(graph_object.yScale)
        .innerTickSize(-graph_object.width)
        .outerTickSize(0)
        .tickPadding(10)
        .orient("left");

    var x = graph_object.xScale;
    var y = graph_object.yScale;

    graph_object.line1 = d3.svg.line()
        .x(function (d) {
            return x(d.date);
        })
        .y(function (d) {
            return y(d.value);
        });

    var xDomain = d3.extent(data, function (d) {
        return d.date;
    });
    var yDomain = d3.extent(data, function (d) {
        return d.value;
    });


    var graph = d3.select("#timeseries_graph").append("svg")
        .attr("width", graph_object.width + graph_object.margin.left + graph_object.margin.right)
        .attr("height", graph_object.height + graph_object.margin.top + graph_object.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + graph_object.margin.left + "," + graph_object.margin.top + ")")
        .style("fill", "#5b4421");

    graph.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + graph_object.height + ")")
        .call(graph_object.xAxis)
        .append("text")
        .attr("class", "axis_label")
        .attr("x", xlabel_x)
        .attr("y", xlabel_y)
        .style("text-anchor", "end")
        .style("fill", "#5b4421")
        .style("font-size", "12pt")
        .text("Time");

    graph.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", graph_object.line1);


    var drag = d3.behavior.drag()
        .on("dragstart", function (d) {
        })
        .on("drag", function (d, i) {
            d.value = y.invert(d3.mouse(this)[1])
            d3.select(this).attr("cy", function (d) {
                return d3.mouse(this)[1];
            });
            d3.select("#v" + (this.id)).text(d.value.toPrecision(2));
            values[i] = d.value;
        })
        .on("dragend", function (d) {
        });

    graph.selectAll(".draggable")
        .data(data)
        .enter().append("circle")
        .style("stroke", "gray")
        .style("fill", "black")
        .attr("id", function (d, i) {
            return i.toString()
        })
        .attr("r", 5)
        .attr("class", "draggable")
        .attr("cx", function (d) {
            return x(d.date);
        })
        .attr("cy", function (d) {
            return y(d.value);
        })
        .call(drag);


}

