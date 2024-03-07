import 'package:flutter/material.dart';
import 'package:tracker_app/widgets/expenses_list/expenses_list.dart';
import 'package:tracker_app/models/expense.dart';

class TrackerApp extends StatefulWidget {
  const TrackerApp({super.key});

  @override
  State<TrackerApp> createState() => _TrackerAppState();
}

class _TrackerAppState extends State<TrackerApp> {
  final List<Expense> _registeredExpenses = [
    Expense(
      title: 'Flutter Coures',
      amount: 19.99,
      date: DateTime.now(),
      category: Category.work,
    ),
    Expense(
      title: 'Cinema',
      amount: 16.99,
      date: DateTime.now(),
      category: Category.leisure,
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter ExpenseTracker'),
          actions: [
            IconButton(
              onPressed: () {},
              icon: const Icon(Icons.add),
            )
          ],
        ),
        body: Column(
          children: [
            const Text('The chart'),
            Expanded(
              child: ExpensesList(expenses: _registeredExpenses),
            ),
          ],
        ),
      ),
    );
  }
}
