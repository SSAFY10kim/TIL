import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:testpro/providers/counts.dart';

import 'package:testpro/providers/counter.dart';
import 'package:testpro/providers/buttons.dart';
import 'package:testpro/providers/memo.dart';
import 'package:testpro/providers/memotext.dart';
import 'package:testpro/providers/test.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => Counts()),
        ChangeNotifierProvider(create: (_) => Memo()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Flutter Provider',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const Home());
  }
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Providers'),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => Counts(),
        child: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Counter(),
              Buttons(),
              TestCounter(),
              MemoText(),
            ],
          ),
        ),
      ),
    );
  }
}
