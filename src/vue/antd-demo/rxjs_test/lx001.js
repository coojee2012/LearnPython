const { Observable,range,of } = require('rxjs');
const { map, filter } = require('rxjs/operators');

of(true).subscribe(x=>{
  console.log(x);
})

range(1, 2).pipe(
  filter(x => x % 2 === 1),
  map(x => x + x)
).subscribe(x => console.log(x));





const observable = new Observable(function subscribe(subscriber) {
    let i = 0;
    const id = setInterval(() => {
            subscriber.next(`hi${i}`)
            i++
    }, 1000);

    return function unsubscribe() {
        clearInterval(id);
      };
  });

const sb = observable.subscribe(x => {
  console.log(x);
  if(x=='hi10'){
    sb.unsubscribe()
  }
});

const sb1 = observable.subscribe(x => {
    console.log(x);
    if(x=='hi20'){
      sb1.unsubscribe()
    }
  });


