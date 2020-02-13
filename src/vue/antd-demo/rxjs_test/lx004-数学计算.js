const { range,from } =  require('rxjs');
const { count,max,min,reduce } = require('rxjs/operators');

const numbers = range(1, 7);
const countresult = numbers.pipe(count(i => i % 2 === 1));
countresult.subscribe(x => console.log(x));
// Results in:
// 4

const maxresult = numbers.pipe(max());
maxresult.subscribe(x => console.log(x));

const minresult = numbers.pipe(min());
minresult.subscribe(x => console.log(x));

const seed = 10;
const countreduce = numbers.pipe(reduce((acc, one) => {
    console.log(acc,one)
    return acc + one
}, seed));
countreduce.subscribe(x => console.log(x));


const obs = from([{a:1,b:2},{c:3,d:4},{e:5,f:6}])
const reduceObj = obs.pipe(
    reduce((acc,one)=>{
        return Object.assign({},acc,one)
    },{})
)

reduceObj.subscribe(x => console.log(x));