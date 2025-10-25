List<String> animals = new ArrayList<>() {{
    add("Кошка");
    add("Собака");
}};

List<String> animals = new ArrayList<>(Arrays.asList("Кошка", "Собака"));

List<String> animals = Stream.of("Кошка", "Собака")
    .collect(Collectors.toList());
