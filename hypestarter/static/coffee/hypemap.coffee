
# Parameters
width = 960
height = 500

# Grab latest tweets from server
get_and_map_locations = (map, projection) ->
    d3.json(
        STATIC_URL + 'locations.json',
        (locations) ->
            i = 0
            for location in locations
                i++
                callback = (current_location) ->
                    return () ->
                        map_location(current_location, map, projection)
                        

                setTimeout(
                    callback(location),
                    i * 2000
                )
    )

# Create map
create_map = () ->
    map = d3.select("#hypemap").append("svg")
    .attr("width", 960)
    .attr("height", 500)
    return map

map_states = (map, projection) ->
    # Project states on map
    path = d3.geo.path().projection(projection);
    d3.json(
        STATIC_URL + 'us-states.json',
        (collection) ->
            map.selectAll('path')
            .data(collection.features)
            .enter().append('path').attr('d', path)
    )
    return map

map_location = (location, map, projection) ->
    coordinates = projection([location[1], location[0]])
    console.debug(coordinates)
    if (coordinates[0] < 5 || coordinates[0] > (width - 5) || coordinates[1] < 5 || coordinates[1] > (width-5))
        return
    add_point(map, coordinates)
# Plot tweet points on map

add_point = (map, coordinates) ->
    rad = 8
    # Ping effect
    map.append('svg:circle')
        .style("stroke", "rgba(255,49,49,.7)")
        .style("stroke-width", 1)
        .style("fill", "rgba(0,0,0,0)")
        .attr('cx', coordinates[0])
        .attr('cy', coordinates[1])
        .attr('r', 5)
        .transition()
            .delay(0)
            .duration(3000)
            .attr("r", 60)
            .style("stroke-width", 2)
            # IE doesn't like the transition to 0 opacity so using a small number (.0001)
            .style("stroke", "rgba(255,49,49,0.0001)")
        .transition()
            .duration(3000)
            .remove()

    # Add circles representing tweets
    map.append('svg:circle')
        .attr("class", "point")
        # Add an id such that each circle is mapped to a number, remove earliest circles once 10 exist on screen
        .style("stroke", "rgba(255,49,49,.7)")
        .style("stroke-width", 1)
        .style("fill", "rgba(240,49,49,1)")
        .attr('cx', coordinates[0])
        .attr('cy', coordinates[1])
        .attr('r', rad)
        .transition()
            .duration(5000)
            .attr("r", 0.0001)
            .remove()

# Main
map = create_map()
projection = d3.geo.albers()
map = map_states(map, projection)
get_and_map_locations(map, projection)