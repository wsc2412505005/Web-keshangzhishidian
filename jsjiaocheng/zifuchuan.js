//js 对象
const user = {
    name:'zhangsan',
    age:18,
    city:'beijing'
}
console.log(user,"js对象");
//json.stringify() 将js对象转换成json字符串
const jsonString = JSON.stringify(user);
console.log(jsonString,'json字符串');
console.log(typeof jsonString,'json字符串的类型');
//json.parse() 将json字符串转换成js对象
const obj = JSON.parse(jsonString);
console.log(obj,'转回对象');
console.log(typeof obj,'转回对象类型');
//赚回来之后可以继续访问属性
console.log(obj.name,'对象中的name');
console.log(obj.age,'对象中的age');
//json也可以表示数组
const arr = ["apple", "banana", "orange"];
const arrJson = JSON.stringify(arr);
console.log(arr,'json数组');
console.log(arrJson,'json数组');
const newArr = JSON.parse(arrJson);
console.log(newArr,'转回数组');
//json特点：json中的键名通常要用双引号
Json = '{title:"jsjsjsj","price":666,"order":"adad"}' 

