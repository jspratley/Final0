$('document').ready(function() {

    var width = 500;
    var height = 400;
    var placeholder = false;
    var contents = null;

    // Creates force layout for visualization
    var force = d3.layout.force()
                .linkDistance(90)
                .charge(-110)
                .gravity(.05)
                .size([width, height])
                .on("tick", tick);

    // Creates container to hold visualization
    var svg = d3.select("#lexicon").append("svg")
                .attr("width", width)
                .attr("height", height);

    var link = svg.selectAll(".link"),
        node = svg.selectAll(".node");

    function update(root) {
        var nodes = flatten(root),
        links = d3.layout.tree().links(nodes);

        force.nodes(nodes)
                .links(links)
                .start();

        link = link.data(links, function(d) { return d.target.id; });
        link.exit().remove();
        link.enter().insert("line", ".node")
                    .attr("class", "link");

        node = node.data(nodes, function(d) { return d.id; });
        node.exit().remove();

        var nodeEnter = node.enter().append("g")
                            .attr("class", "node")
                            .on("click", click)
                            .call(force.drag);

        nodeEnter.append("circle")
                .attr("r", function(d) { return 28; });

        nodeEnter.append("text")
                .attr("dy", ".35em")
                .text(function(d) { return d.name; });

        node.select("circle")
            .style("fill", color);
    }

    function tick() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    }

    function color(d) {
        return d._children ? "#3182bd"
                : d.children? "#c6dbef"
                : "#d76a6a";
    }

    function click(d) {
        if (d3.event.defaultPrevented) return;
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = d._children;
            d._children = null;
        }
        update();
    }

    function flatten(root) {
        var nodes = [], i = 0;

        function recurse(node) {
            if (node.children) node.children.forEach(recurse);
            if (!node.id) node.id = ++i;
            nodes.push(node);
        }

        recurse(root);
        return nodes;
    }

    $.getJSON($SCRIPT_ROOT + '/lex', function(data) {
        root = data.word_cats;
        update(root);
    });

    // This function is supposed to send data to the backend and retrieve it from the front end
    $('#share').on('click', function() {
        if ($('#upload')[0].files.length == 0 && $('textarea[name="sent"]').val() == null) {
            alert('Please enter some data.');
            return;
        }
        else if ($('#upload')[0].files.length == 0) {
            $.getJSON($SCRIPT_ROOT + '/submit', {
                sentence: $('textarea[name="sent"]').val(),
                file: "",
                order: $('input[name="ord"]').val()
            }, function(data) {
                root = data.word_cats;
                update(root);
                $('#prod_sentence').empty();
                $('#prod_sentence').append('<p>' + data.new_sent + '</p>');
            });
        }
        else {
            getFileText($('#upload')[0].files[0], function(e) {
                $.getJSON($SCRIPT_ROOT + '/submit', {
                    sentence: $('textarea[name="sent"]').val(),
                    file: e.target.result,
                    order: $('input[name="ord"]').val()
                }, function(data) {
                    root = data.word_cats;
                    update(root);
                    $('#prod_sentence').empty();
                    $('#prod_sentence').append('<p>' + data.new_sent + '</p>');
                });
            });
        }
    });

    function getFileText(file, onLoadText) {

        if (!file) {
            return null;
        }

        fr = new FileReader();
        fr.onload = onLoadText;
        fr.readAsText(file);
    }

});