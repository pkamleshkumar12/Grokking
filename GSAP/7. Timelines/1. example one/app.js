var tl= gsap.timeline({
    defaults: {
        duration: 1,
    }
})

tl.to(".box1",{
    scale: 0, 
    opacity: 0,
    delay: 1
}).to(".box2", {
    x: -200,
}).to(".box3", {
    x: -200,
    borderRadius: 0, 
    rotate: 360
}).set(".box1",{
    x:200,
}).to(".box1", {
    scale: 1,
    opacity: 1
})