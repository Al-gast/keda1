window.onload = function () {
    $(document).ready(function () {

        //untuk loadmore career
        var $career = 4;
        $("[name='loadMoreCareer']").click(function () {
            var $sumCareer = $("[name='loadMoreCareer']").val()
            $(".career").find('.hidden'); // selects all hidden comments
            $(".career").slice(0, $career).fadeIn().removeClass('hidden');// removes 'd-none' class
            $career = $career + 4;

            if ($career >= $sumCareer) {
                $("[name='loadMoreCareer']").fadeOut().addClass('hidden');
            }

        });

        const input = document.getElementById('searchCareer');
        input.addEventListener('keyup', (e) => {
            var inputs = e.target.value.toLowerCase(); //do lowercase
            //loop through outer div and hide it
            var inputsLength = e.target.value.length;

            console.log(inputsLength);

            if (inputsLength < 1) {
                $('#loadMoreCareer').show();
                $(".career").slice(0, $career).fadeOut().addClass('hidden');
            } else {
                $('#loadMoreCareer').hide();
                $(".career").find('.hidden'); // selects all hidden comments
                $(".career").slice(0, $career).fadeIn().removeClass('hidden');
            }


            //searchcareer
            document.querySelectorAll('.outers').forEach(function (el) {
                el.style.visibility = "hidden";
                el.style.display = 'none';
            });
            //loop through outer ->card-title
            document.querySelectorAll('.outers .card-title').forEach(function (el) {
                //compare 
                if (el.textContent.toLowerCase().indexOf(inputs) > -1) {
                    el.closest('.outers').style.visibility = 'visible';
                    el.closest('.outers').style.display = 'block';
                    //if match show that div
                }

            });

            document.querySelectorAll('.outers .career-tag').forEach(function (el) {
                //compare 
                if (el.textContent.toLowerCase().indexOf(inputs) > -1) {
                    el.closest('.outers').style.visibility = 'visible';
                    el.closest('.outers').style.display = 'block';
                    //if match show that div
                }

            });
            //end of searchcareer
        });
        // //end of searchcareer
        // let buttons = document.querySelectorAll(".copyClipboard"); // quaryselectorall will return and nodelist of button with classnaem .unLockUser-button
        // buttons.forEach((btn, index) => {// index will be current button index
        //     btn.addEventListener("click", function (e) {
        //         console.log(e.target, index);
        //         console.log('hallo');
        //     });
        // })


        // $.each($('.copyClipboard'), function (i, val) {
        //     var copyText = $(this).val();
        //     console.log(copyText);
        // });


    }); // end document ready


}