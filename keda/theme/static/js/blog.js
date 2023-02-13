window.onload = function () {
    $(document).ready(function () {
        //untuk loadmore blog
        var $blog = 3;
        $("[name='loadMore']").click(function () {
            var $sumBlog = $("[name='loadMore']").val()
            $(".blog").find('.hidden'); // selects all hidden comments
            $(".blog").slice(0, $blog).fadeIn().removeClass('hidden');// removes 'd-none' class
            $blog = $blog + 2;

            if ($blog >= $sumBlog) {
                $("[name='loadMore']").fadeOut().addClass('hidden');
            }

        });
        //start of searchblog
        const inputBlog = document.getElementById('searchBlog');
        inputBlog.addEventListener('keyup', (e) => {
            var inputBlog = e.target.value.toLowerCase(); //do lowercase
            //loop through outer div and hide it
            var inputsBlogLength = e.target.value.length;

            console.log(inputsBlogLength);

            if (inputsBlogLength < 1) {
                $('#loadMore').show();
                $(".blog").slice(0, $blog).fadeOut().addClass('hidden');
            } else {
                $('#loadMore').hide();
                $(".blog").find('.hidden'); // selects all hidden comments
                $(".blog").slice(0, $blog).fadeIn().removeClass('hidden');
            }


            //searchblog
            document.querySelectorAll('.outersBlog').forEach(function (el) {
                el.style.visibility = "hidden";
                el.style.display = 'none';
            });
            //loop through outer ->card-title
            document.querySelectorAll('.outersBlog .blogTag').forEach(function (el) {
                //compare 
                if (el.textContent.toLowerCase().indexOf(inputBlog) > -1) {

                    el.closest('.outersBlog').style.visibility = 'visible';
                    el.closest('.outersBlog').style.display = 'block';
                    //if match show that div
                }

            });

            document.querySelectorAll('.outersBlog .blogTitle').forEach(function (el) {
                //compare 
                if (el.textContent.toLowerCase().indexOf(inputBlog) > -1) {

                    el.closest('.outersBlog').style.visibility = 'visible';
                    el.closest('.outersBlog').style.display = 'block';
                    //if match show that div
                }

            });
            //end of searchblog
        });
    }); // end document ready

}