const { range,from,of,Subject,EMPTY } =  require('rxjs');
const { every,find,findIndex,isEmpty,defaultIfEmpty } = require('rxjs/operators');

of(1,2,4,5,6).pipe(
    every(x => x < 5),
)
.subscribe(x => console.log(x)); // -> false


of(1,2,4,5,6).pipe(
    find(x => x > 4), //只返回符合条件的第一个数据
)
.subscribe(x => console.log(x)); // -> 5

of(1,2,4,5,6).pipe(
    findIndex(x => x > 4), //只返回符合条件的第一个数据的索引，从0开始，如果找不到有效值，不会发出错误。
)
.subscribe(x => console.log(x)); // -> 5


const source = new Subject();
const result = source.pipe(isEmpty());
source.subscribe(x => console.log(x));
result.subscribe(x => console.log(x)); //在收到a之后返回false
source.next('a');
source.next('b');
source.next('c');
source.complete();

const result2 = EMPTY.pipe(isEmpty());
result2.subscribe(x => console.log(x));
// Results in:
// true

const result3 = EMPTY.pipe(defaultIfEmpty('default If Empty'));
result3.subscribe(x => console.log(x));