// JavaScript Document
/*
$("").mChange({
	auto  : 1,       //鏄惁鑷姩鎾斁,1涓鸿嚜鍔�,0涓烘墜鍔�
	arrow : 1,       //鏄惁鍙嶈浆绠ご,1涓虹偣鍑诲乏渚у悜鍙虫粴鍔�,0鍒欑浉鍙�
	speed : 500,     //鏁堟灉閫熷害,澶т簬0.3
	time  : 5000,    //鍛ㄦ湡鏃堕棿锛屽ぇ浜�1
	nav   : null,    //瀵艰埅
	nave  : "click", //瀵艰埅浜嬩欢
	navs  : 0,  //瀵艰埅婊氬姩
	prev  : null,    //涓婁竴涓�
	next  : null,    //涓嬩竴涓�
	cycle : 1,       //鏄惁寰幆
	mousestop : 0,   //鏄惁榧犳爣鍒掑叆鍋滄
	mousewheel : 0,  //鏄惁寮€鍚粴杞簨浠�
	count : null,    //鎬绘暟
	index : null,    //褰撳墠
	fnCome: null,    //鍥炶皟鍓嶅嚱鏁�
	fnBack: null     //鍥炶皟鍑芥暟
});
*/
(function($) {
	$.fn.mChange = function(options) {
		var w1,np,ns,v;
		var opts = $.extend({},$.fn.mChange.defaults,options); 
		//鍒濆鍖�
		var c=$(this);
		var f=c.parent();
		var n=$(opts.nav);
		var i=0;
		var sw=1;
		c.hide();
		
		if(opts.navs){
			w1 = n.outerWidth()+(parseInt(n.css("margin-left"))?parseInt(n.css("margin-left")):0)+(parseInt(n.css("margin-right"))?parseInt(n.css("margin-right")):0);
			np= $(opts.nav).parent();
			n.wrapAll("<div class='scroll' style='height:100%;'></div>");
			ns=np.find(".scroll");
			ns.width(n.length*w1);
			np.stop().animate({scrollLeft:0},100);
		}
			
		function run(){
			if(sw){
				i++;
				i=change(i);
			}
		}
		
		$(opts.count).text(c.length);
		
		function change(idx){
			if(c.length>1 || idx=="begin"){
				sw=0;
				if(idx=="begin"){
					idx=0;
					speed=0;
				}
				else{
					speed=opts.speed;
					c.stop(true,true).fadeOut(speed);
				}
				
				n.removeClass("now");
				if(idx==c.length){idx=0;}
				if(idx<0){idx=c.length-1;}
				
				
				$(opts.index).text(idx+1);
				
				c.eq(idx).stop().fadeIn(speed,function(){
					if(typeof(opts.fnBack)=="function"){
						opts.fnBack(idx);//鎵ц鑷畾涔夊姩鐢�2
					}
					sw=1;
				});
				if(typeof(opts.fnCome)=="function"){
					opts.fnCome(idx);//鎵ц鑷畾涔夊姩鐢�1
				}
				
				n.eq(idx).addClass("now");			
				if(opts.navs){autonav(idx);}
				
				return idx;
			}
		}
		change("begin");
		
		if(opts.auto==1){
			v=setInterval(run,opts.time);
		}
		
		if(opts.mousestop==1){
			c.hover(
				function(){sw=0;},
				function(){sw=1;}
			);
		}
		
		//瀵艰埅婧㈠嚭閮ㄥ垎婊戝姩鏄剧ず
		function autonav(idx){
			np.animate({scrollLeft:idx*w1});
		}
			
		n.each(function(index, element) {
            $(this).bind(opts.nave,function(){
				if(c.eq(index).length>0){
					change(index);
					i=index;
					if(opts.auto){
						clearInterval(v);
						v=setInterval(run,opts.time);
					}
				}
			});
        });
		
		$(opts.prev).click(function(){
			if(sw==1){
				if(opts.cycle==1 || (opts.cycle==0 && i>0)){
					i--;
					i=change(i);
					if(opts.auto==1){
						clearInterval(v);
						v=setInterval(run,opts.time);
					}
				}
			}
		});
		$(opts.next).click(function(){
			if(sw==1){
				if(opts.cycle==1 || (opts.cycle==0 && i<c.length-1)){
					i++;
					i=change(i);
					if(opts.auto){
						clearInterval(v);
						v=setInterval(run,opts.time);
					}
				}
			}
		});
		
		if(opts.mousewheel){
			f.mousewheel(function(event,delta,deltaX,deltaY){
				if(delta<0){
					if(sw==1){
						if(opts.cycle==1 || (opts.cycle==0 && i<c.length-1)){
							i++;
							i=change(i);
							if(opts.auto){
								clearInterval(v);
								v=setInterval(run,opts.time);
							}
						}
					}
				}
				else{
					if(sw==1){
						if(opts.cycle==1 || (opts.cycle==0 && i>0)){
							i--;
							i=change(i);
							if(opts.auto){
								clearInterval(v);
								v=setInterval(run,opts.time);
							}
						}
					}
				}
				event.stopPropagation();
				event.preventDefault();
			});
		}
			
	};
	$.fn.mChange.defaults = {
		auto  : 1,
		arrow : 1,
		speed : 800,
		time  : 5000,
		nav   : null,
		nave  : "click",
        navs  : 0,
		prev  : null,
		next  : null,
		cycle : 1,
		mousestop : 0,
	    mousewheel : 0,
		count : null,
		index : null,
		fnCome: null,
		fnBack: null
	}
})(jQuery);