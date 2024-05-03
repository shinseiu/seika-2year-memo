document.addEventListener("DOMContentLoaded", function() {
	// 获取图片元素
	var image1 = document.getElementById("image1");
	var image2 = document.getElementById("image2");
    
	// 使用 Anime.js 创建旋转动画
	//anime({
	//targets: [image1,image2],
	//rotate: '1turn', // 旋转一周 (360度)
	//duration: 5000, // 动画持续时间为 5 秒
	//easing: 'linear', // 使用线性缓动函数控制动画速度
	//translateX: '100px', // 将球体向右移动 500px
    	//translateY: '200px', // 向下移动 200px
    	//duration: 5000, // 动画持续时间为 1 秒
    	//easing: 'easeOutQuad', // 使用缓动函数控制动画速度
    	//direction: 'alternate', // 反向播放动画
	//loop: true // 循环播放动画
	//});
		// 使用 Anime.js 创建不规则运动动画
	anime({
	targets: [image1,image2],
		translateX: function() {
		    return anime.random(-250, 250); // 随机生成 translateX 值
		},
		translateY: function() {
		    return anime.random(-250, 250); // 随机生成 translateY 值
		},
		duration: function() {
		    return anime.random(1000, 3000); // 随机生成动画持续时间
		},
		  easing: 'easeInOutQuad', // 使用缓动函数控制动画速度
		complete: function() {
		    // 动画完成后重新执行动画
		animateImage();
		}
		});
	    
		// 执行动画函数
	function animateImage() {
		anime({
			targets: [image1,image2],
		translateX: function() {
			return anime.random(-250, 250); // 随机生成 translateX 值
		    },
		    translateY: function() {
			return anime.random(-250, 250); // 随机生成 translateY 值
		    },
		    duration: function() {
			return anime.random(1000, 3000); // 随机生成动画持续时间
		    },
		    easing: 'easeInOutQuad', // 使用缓动函数控制动画速度
		    complete: function() {
			// 动画完成后重新执行动画
			animateImage();
		    }
		  });
		}
	    
		// 第一次执行动画
		animateImage();
	    });
    