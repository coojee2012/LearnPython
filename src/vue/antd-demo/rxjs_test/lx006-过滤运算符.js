const { range,from,of,Subject,EMPTY,interval,asyncScheduler } =  require('rxjs');
const { first,auditTime,audit,take,tap, throttleTime } = require('rxjs/operators');

// first
// 仅发出源Observable发出的第一个值（或满足某些条件的第一个值）。

range(1,100).pipe(first((x) => {
return x%3 === 2 && x>50
})).subscribe(x=>{
    console.log(x)
})

const test1$ = interval(1000).pipe(take(10))

const test11$ = test1$.pipe(
    auditTime(2000));
test11$.subscribe(x=>{console.log('auditTime sub:',x)})

const test12$ = test1$.pipe(
            audit((x) => {
                return interval(3000)
            })
    );
test12$.subscribe(x=>{console.log('audit sub:',x)})


// defaultThottleConfig = { leading: true, trailing: false }
const throttleConfig = {
    leading: false,
    trailing: true
  }

const doubleClick = test1$.pipe(
    throttleTime(400, asyncScheduler, throttleConfig)
  );
   
doubleClick.subscribe((throttleValue) => {
    console.log(`Double-clicked! Timestamp: ${throttleValue.timeStamp}`);
  });