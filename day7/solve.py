def get_data():
    bags = {}

    data_file = open("data.txt")

    for val in data_file:
        # <color> "bags contain" ["no other bags." or one or more <number> <color> "bag(s)[],.]"]
        # bright salmon bags contain 5 shiny orange bags, 2 dark yellow bags, 5 muted gold bags, 4 dark fuchsia bags.
        bg_data = val.split(' bags contain ')
        bag_color = str(bg_data[0])

        bag_data = []
        bag_counts = []
        bag_colors = []
        if bg_data[1].strip() != 'no other bags.':
            # parse list of bags
            bag_list = bg_data[1][:-2].split(',')
            for bag in bag_list:
                bag_info = bag.strip().split(' ')
                inside_bag_count = int(bag_info[0])
                inside_bag_color = bag_info[1] + " " + bag_info[2]
                bag_data.append((inside_bag_count, inside_bag_color))
                bag_counts.append(inside_bag_count)
                bag_colors.append(inside_bag_color)
        bags[bag_color] = (bag_counts, bag_colors)
        # if bag_color == 'shiny gold' or bag_color == 'dark lavender':
        #     print(bag_color, bags[bag_color])
        #     print(val)
    data_file.close()

    return bags


def check_bags(bags, gold_bags, bag_list_to_check):
    # function finds all bags that can contain bags that are
    # finds backs that are in the to check list, that can contain
    # a bag that can contain gold - the gold bags.
    new_gold_bags = set()
    for bag in bag_list_to_check:
        print(f"Checking {bag}")
        for bag_color, bag_contents in bags.items():
            if bag in bag_contents[1]:
                new_gold_bags.add(bag_color)
                print(
                    f"    {bag_color}, can hold a {bag} bag that holds gold.")

    return new_gold_bags


def find_bag_count_inside(bags, bag_color, depth):
    bag_counts, bag_colors = bags[bag_color]

    if len(bag_colors) == 0:
        bag_total = 0
    else:
        bag_total = 0
        for idx in range(len(bag_colors)):
            bag_total += bag_counts[idx] + (bag_counts[idx] *
                                            find_bag_count_inside(bags, bag_colors[idx], depth+1))

    print('-' * depth, bag_color, len(bag_colors), bag_total, bag_colors)
    return bag_total


def check_data2(bags):
    top_bag_color = 'shiny gold'  # shiny gold'
    print(f"\nSearching for total count inside {top_bag_color}")

    depth = 0
    bag_counts, bag_colors = bags[top_bag_color]
    bag_count = 0
    print(bag_counts, bag_colors)
    for idx in range(len(bag_colors)):
        print(bag_colors[idx])
        # for each bag, count all bags inside it.
        bag_count += bag_counts[idx] + (bag_counts[idx] *
                                        find_bag_count_inside(bags, bag_colors[idx], depth+1))

    print(f"total bags: {bag_count}")


def check_data(bags):
    print("shiny gold!", bags['shiny gold'])

    total_count = 0
    gold_bags = set()
    # first find bags that can contain shiny gold
    found_bags_with_gold = set()
    for bag_color, bag_contents in bags.items():
        if 'shiny gold' in bag_contents[1]:
            total_count += 1
            found_bags_with_gold.add(bag_color)
            gold_bags.add(bag_color)
            print(f"{total_count:2d}  {bag_color} can hold gold.")

    # special case.
    # if 'shiny gold' in found_bags_with_gold:
    #     found_bags_with_gold.remove('shiny gold')

    # now look for bags that can contain any bag that can contain gold :)
    recursions = 300
    while True and recursions > 0:
        new_bags_with_gold = check_bags(bags, found_bags_with_gold, gold_bags)
        bag_count = len(new_bags_with_gold)
        print(f"found {len(new_bags_with_gold)} more bags.")
        if bag_count > 0:
            found_bags_with_gold = found_bags_with_gold.union(
                new_bags_with_gold)
            gold_bags = new_bags_with_gold
            print(
                f"\nTotal Bags found: {len(found_bags_with_gold)} after adding the new {len(new_bags_with_gold)}")
        else:
            break
        recursions -= 1

    print(
        f"\nTotal Bags that can hold 'shiny gold': {len(found_bags_with_gold)}")


def main():
    data = get_data()
    check_data(data)
    check_data2(data)


main()
