// Scroll to top when user switched tab
$(function()
{
      $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
      $(window).scrollTop(0);
      if( $(e.target).attr('href') === '#section-project' )
      {
        listItem = document.getElementById("all-filter");
        listItem.click();
      }
    })
});

// More about me
var btn_home_moreabtme = document.getElementById('btn_home_moreabtme');
btn_home_moreabtme.onclick = function(){
    document.getElementById("nav_about").click();
};

(function() {

	var projectMasonry = function() {
 $('.filters ul li').click(function(){
        var x = document.querySelectorAll("li[data-filter]");

        x.forEach(item => {
                  if( item.textContent == this.textContent )
                  {
                    $(item).addClass('active');
                  }
                  else
                  {
                    $(item).removeClass('active');
                  }
        });
        var data = $(this).attr('data-filter');
        $grid.isotope({
          filter: data
        })
      });

      if(document.getElementById("section-project")){
            var $grid = $(".grid").isotope({
              itemSelector: ".all",
              percentPosition: true,
              masonry: {
                columnWidth: ".all"
              }
            })
      };


	};


	$(function(){
		projectMasonry();
	});

})();


// Skill cloud
$(document).ready(() => {
    list = [['C++', 40], ['Python', 40], ['Apache', 30],['Django', 30],['Tensorflow', 30], ['sklearn', 30], ['UTF', 30]]
    WordCloud(document.getElementById('canvasSkillCloud'), { list: list, minRotation: 0, maxRotation: 0 } );
})
