import { useSelector, useDispatch } from 'react-redux';
import { useState } from 'react';

import { counterActions } from '../store/counter.jsx';
import classes from './Counter.module.css';

const Counter = () => {
  const [value, setValue] = useState();

  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter.counter);
  const show = useSelector((state) => state.counter.showCounter);

  const incrementHandler = () => {
    dispatch(counterActions.increment());
  };

  const increseHandler = () => {
    const numericValue = parseInt(value, 10) || 0;

    // Redux store에 해당 값을 반영합니다.
    dispatch(counterActions.increse(numericValue));

    // value 상태를 초기화합니다.
    setValue('');
  };

  const decrementHandler = () => {
    dispatch(counterActions.decrement());
  };

  const toggleCounterHandler = () => {
    dispatch(counterActions.toggleCounter());
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {show && <div className={classes.value}>{counter}</div>}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={increseHandler}>Increment 5</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
      <div>
        <input
          type="number"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
