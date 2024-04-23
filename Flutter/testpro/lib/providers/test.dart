import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:testpro/providers/counts.dart';

class TestCounter extends StatelessWidget {
  const TestCounter({super.key});

  @override
  Widget build(BuildContext context) {
    return Text(
      context.read<Counts>().count.toString(),
      style: const TextStyle(fontSize: 30),
    );
  }
}
