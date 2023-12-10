def degrees_of_separation(relationships, name1, name2)
  graph = Hash.new { |hash, key| hash[key] = [] }

  # Build the graph from the relationships
  relationships.each do |relationship|
    person1, person2 = relationship.split(':')
    graph[person1] << person2
    graph[person2] << person1
  end

  # p graph

  visited = {}
  queue = [[name1, 0]]

  puts "\nqueue"
  p queue

  while queue.any?
    current, degrees = queue.shift
    visited[current] = true
    puts "\nvisited"
    p visited
    puts "\ncurrent"
    p current
    puts "\ndegrees"
    p degrees
    puts "----"

    return degrees if current == name2

    graph[current].each do |neighbor|
      queue << [neighbor, degrees + 1] unless visited[neighbor]
    end
  end

  puts "\ngraph"
  p graph

  # If no path is found
  -1
end

# Example usage
relationships = ['fred:joe', 'mary:fred', 'mary:bill']
result = degrees_of_separation(relationships, 'fred', 'bill')
# puts result
