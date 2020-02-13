const { interval } = require('rxjs');
const { map,take,concatAll,mergeAll } = require('rxjs/operators');

const hot$ = interval(1000).pipe(
    take(2),
    map(x => {
        console.log('1',x)
        return interval(1500).pipe(
        map(y => {
        console.log('2',y)
           return  x+':'+y
        }),
        take(2)
        )
    })
)

const concated$ = hot$.pipe(concatAll())
const mergeAll$ = hot$.pipe(mergeAll())

// concated$.subscribe(x => {
//     console.log('concated$:',x)
// })

mergeAll$.subscribe(x => {
    console.log('mergeAll$:',x)
})
