const { Observable,range,of } = require('rxjs');
const { map, filter,first } = require('rxjs/operators');
const a  = map(x => x * x)
console.log(a);

const a$ = a(of(1, 2, 3))
console.log(a$);
const c = a$.subscribe((v) => console.log(`value: ${v}`));


first()(of(1, 2, 3)).subscribe((v) => console.log(`value: ${v}`));
