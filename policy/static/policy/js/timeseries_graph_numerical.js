function timeseries_graph_numerical(title, dates, values, metrics) {

    d3.select("#timeseries_graph").html("");

    let parseTime = d3.time.format("%Y-%m-%d");
    let data = [];
    for (let k = 0; k < dates.length; k++) {
        data.push({'date': parseTime.parse(dates[k]), 'value': values[k]})
    }

    let max_val = Math.max.apply(Math, values);
    let min_val = Math.min.apply(Math, values);

    let graph_object = {};
    graph_object.margin = {top: 50, right: 50, bottom: 50, left: 50};
    graph_object.width = 750 - graph_object.margin.left - graph_object.margin.right;
    graph_object.height = 450 - graph_object.margin.top - graph_object.margin.bottom;

    let xlabel_y = 40;
    let xlabel_x = graph_object.width / 2 + 20;

    let ylabel_y = -20;
    let ylabel_x = 200 + graph_object.width / 2;

    graph_object.x = d3.time.scale()
        .domain(d3.extent(data, function (d) {
            return d.date;
        }))
        .range([0, graph_object.width]);

    let ext = d3.extent(data, function (d) {
        return d.value;
    })
    graph_object.y = d3.scale.linear()
        .domain([0.95 * min_val, 1.05 * max_val])
        .range([graph_object.height, 0]);

    let x = graph_object.x
    let y = graph_object.y

    graph_object.xAxis = d3.svg.axis()
        .scale(graph_object.x)
        .innerTickSize(-graph_object.height)
        .outerTickSize(0)
        .tickPadding(10)
        .tickFormat(d3.timeFormat("%b"))
        .orient("bottom");

    graph_object.yAxisL = d3.svg.axis()
        .scale(graph_object.y)
        .innerTickSize(-graph_object.width)
        .outerTickSize(0)
        .tickPadding(10)
        .tickFormat(formatValue)
        .orient("left");

    graph_object.line1 = d3.svg.line()
        .x(function (d) {
            return x(d.date);
        })
        .y(function (d) {
            return y(d.value);
        });

    graph_object.yAxisR = d3.svg.axis()
        .scale(graph_object.y)
        .tickValues([metrics['Median'], metrics['Q25'], metrics['Q75'], metrics['T'], metrics['Max'], metrics['Min']])
        .tickFormat(formatValue)
        .orient("right");

    let xDomain = d3.extent(data, function (d) {
        return d.date;
    })
    let yDomain = d3.extent(data, function (d) {
        return d.value;
    });

    let xScale = d3.time.scale().range([0, graph_object.width]).domain(xDomain);
    let yScale = d3.scale.linear().range([graph_object.height, 0]).domain([0.95 * min_val, 1.05 * max_val]);

    let bisectDate = d3.bisector(function (d) {
        return d.date;
    }).left;

    let svg_graph = d3.select("#timeseries_graph").append("svg")
        .attr("width", graph_object.width + graph_object.margin.left + graph_object.margin.right)
        .attr("height", graph_object.height + graph_object.margin.top + graph_object.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + graph_object.margin.left + "," + graph_object.margin.top + ")")
        .style("fill", "#5b4421");

    svg_graph.append("g")
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

    svg_graph.append("g")
        .attr("class", "y axis")
        .call(graph_object.yAxisL)
        .append("text")
        .attr("transform", "translate(0," + 0 + ")")
        .attr("class", "axis_label")
        .attr("y", ylabel_y)
        .attr("x", ylabel_x)
        .style("fill", "#5b4421")
        .style("font-size", "12pt")
        .style("text-anchor", "end")
        .text(title + " x " + Math.pow(10, metrics['Orders'] - 1));

    svg_graph.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + graph_object.width + ",0)")
        .call(graph_object.yAxisR)

    svg_graph.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", graph_object.line1);

    svg_graph.append("line")
        .attr({
            x1: x(parseTime.parse(dates[0])), y1: y(metrics['Median']),
            x2: x(parseTime.parse(dates[data.length - 1])), y2: y(metrics['Median'])
        })
        .attr("stroke-dasharray", ("3, 3"))
        .attr("stroke-width", 1)
        .style("fill", "#5b4421")
        .attr("stroke", "black");

    svg_graph.append("line")
        .attr({
            x1: x(parseTime.parse(dates[0])), y1: y(metrics['Q25']),
            x2: x(parseTime.parse(dates[data.length - 1])), y2: y(metrics['Q25'])
        })
        .attr("stroke-dasharray", ("3, 3"))
        .attr("stroke-width", 1)
        .style("fill", "#5b4421")
        .attr("stroke", "black");

    svg_graph.append("line")
        .attr({
            x1: x(parseTime.parse(dates[0])), y1: y(metrics['Q75']),
            x2: x(parseTime.parse(dates[data.length - 1])), y2: y(metrics['Q75'])
        })
        .attr("stroke-dasharray", ("3, 3"))
        .attr("stroke-width", 1)
        .style("fill", "#5b4421")
        .attr("stroke", "black");

    let focus = svg_graph.append('g').style('display', 'none');

    focus.append('line')
        .attr('id', 'focusLineX')
        .attr('class', 'focusLine');
    focus.append('line')
        .attr('id', 'focusLineY')
        .attr('class', 'focusLine');
    focus.append('circle')
        .attr('id', 'focusCircle')
        .attr('r', 5)
        .attr('class', 'circle focusCircle');

    svg_graph.append('rect')
        .attr('class', 'overlay')
        .attr('width', graph_object.width)
        .attr('height', graph_object.height)
        .on('mouseover', function () {
            focus.style('display', null);
        })
        .on('mouseout', function () {
            focus.style('display', 'none');
        })
        .on('mousemove', function () {
            let mouse = d3.mouse(this);
            let mouseDate = xScale.invert(mouse[0]);
            let i = bisectDate(data, mouseDate);
            let d0 = data[i - 1]
            let d1 = data[i];
            let d = mouseDate - d0.date > d1.date - mouseDate ? d1 : d0;
            let x = xScale(d.date);
            let y = yScale(d.value);

            focus.select('#focusCircle')
                .attr('cx', x)
                .attr('cy', y);
            focus.select('#focusLineX')
                .attr('x1', x).attr('y1', yScale(yDomain[0]))
                .attr('x2', x).attr('y2', yScale(yDomain[1]));
            focus.select('#focusLineY')
                .attr('x1', xScale(xDomain[0])).attr('y1', y)
                .attr('x2', xScale(xDomain[1])).attr('y2', y);

            d3.select("#date_element").html(dates[i])
            d3.select("#value_element").html(d1.value)
        });

    function formatValue(d) {
        let formatNumber = d3.format(".1f%");
        // let s = formatNumber(d);
        let s = formatNumber(d / Math.pow(10, metrics['Orders'] - 1));
        return s;
    }

}

