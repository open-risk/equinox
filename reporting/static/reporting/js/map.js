function getMaxOfArray(numArray) {
    return Math.max.apply(null, numArray);
}

function getMinOfArray(numArray) {
    return Math.min.apply(null, numArray);
}

function initializeMap(dataset, context) {
    let color = d3.scale.linear().domain([context.min_value, context.max_value]).range(["green", "red"]);
    let map = d3.select("#svg_map");
    map.selectAll("path").style("fill", function (i) {
        let old_value = d3.select(this).style("fill");
        if (context.ids.indexOf(this.id) > -1) {
            let value = dataset[this.id].values;
            if (!value) {
                return "gray";
            } else {
                // return color(value);
                return "red";
            }
        } else {
            return old_value;
        }
    });
}