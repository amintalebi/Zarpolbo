$("#search-form").on('submit', function (e) {
    e.preventDefault();
    search();
});

$(".tt-susggestion").on('click', function (e) {
    e.preventDefault();
    search();
});

function search() {
    $this = $("#search-form");
    $.get($this.prop('action'), $this.serialize(), function (data) {

        $("#container").empty();
        for (cafe of data) {
            $("#container").append(`
                    <h1 class="text">${cafe.fields.name}</h1>
                    <img src="${cafe.fields.main_image_url}" alt="Avatar" class="image">
                    <div class="middle">
                    <div class="h-text">${cafe.fields.description}</div>
                    </div>
                    <br/>
                `);
        }

    }, "json");
}