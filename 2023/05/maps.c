
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

struct map_entry {
  unsigned long int src;
  unsigned long int dst;
  unsigned long int length;
};

struct map {
  const char *srcname;
  const char *dstname;
  int map_count;
  const struct map_entry maps[];
};

const struct map seed_soil_map = {
  .srcname = "seed",
  .dstname = "soil",
  .map_count = 10,
  .maps = {{.src = 3725495029, .dst = 3566547172, .length = 569472267},
           {.src = 1249510998, .dst = 2346761246, .length = 267846697},
           {.src = 937956667, .dst = 1812605508, .length = 271194541},
           {.src = 1209151208, .dst = 1421378697, .length = 40359790},
           {.src = 2788751092, .dst = 2083800049, .length = 262961197},
           {.src = 473979048, .dst = 2938601691, .length = 463977619},
           {.src = 1517357695, .dst = 473979048, .length = 947399649},
           {.src = 3566547172, .dst = 4136019439, .length = 158947857},
           {.src = 3051712289, .dst = 1461738487, .length = 350867021},
           {.src = 2464757344, .dst = 2614607943, .length = 323993748}},
};
const struct map soil_fertilizer_map = {
  .srcname = "soil",
  .dstname = "fertilizer",
  .map_count = 9,
  .maps = {{.src = 2583931429, .dst = 3107230831, .length = 576709409},
           {.src = 608291332, .dst = 970181981, .length = 1441137369},
           {.src = 3859046283, .dst = 743954495, .length = 158951815},
           {.src = 3227916509, .dst = 3683940240, .length = 91282070},
           {.src = 2448268266, .dst = 608291332, .length = 135663163},
           {.src = 2049428701, .dst = 3775222310, .length = 398839565},
           {.src = 3319198579, .dst = 2411319350, .length = 539847704},
           {.src = 4017998098, .dst = 2951167054, .length = 156063777},
           {.src = 3160640838, .dst = 902906310, .length = 67275671}},
};
const struct map fertilizer_water_map = {
  .srcname = "fertilizer",
  .dstname = "water",
  .map_count = 42,
  .maps = {{.src = 395703749, .dst = 1257642402, .length = 69589612},
           {.src = 2215701547, .dst = 1800674, .length = 90550534},
           {.src = 358464863, .dst = 2757853693, .length = 37238886},
           {.src = 181079109, .dst = 3285451399, .length = 43937782},
           {.src = 3513448371, .dst = 2346544130, .length = 192150886},
           {.src = 4231433060, .dst = 3866348216, .length = 63534236},
           {.src = 1560332334, .dst = 1327232014, .length = 90281838},
           {.src = 616206288, .dst = 2538695016, .length = 114467702},
           {.src = 225016891, .dst = 255018176, .length = 46372244},
           {.src = 3705599257, .dst = 1171065990, .length = 27021880},
           {.src = 730673990, .dst = 1070753744, .length = 442780},
           {.src = 3479799203, .dst = 221369008, .length = 33649168},
           {.src = 271389135, .dst = 2987721226, .length = 80072982},
           {.src = 732917444, .dst = 1198087870, .length = 24556356},
           {.src = 2306252081, .dst = 199036270, .length = 22332738},
           {.src = 731116770, .dst = 0, .length = 1800674},
           {.src = 3989920675, .dst = 3929882452, .length = 212758268},
           {.src = 757473800, .dst = 631506549, .length = 322942578},
           {.src = 0, .dst = 301390420, .length = 157952443},
           {.src = 157952443, .dst = 2795092579, .length = 1997721},
           {.src = 2619085211, .dst = 1222644226, .length = 34998176},
           {.src = 499901671, .dst = 954449127, .length = 116304617},
           {.src = 159950164, .dst = 1429766246, .length = 21128945},
           {.src = 2074649638, .dst = 2205492221, .length = 141051909},
           {.src = 3732621137, .dst = 2749302577, .length = 8551116},
           {.src = 1219863414, .dst = 459342863, .length = 57737723},
           {.src = 3741172253, .dst = 3329389181, .length = 59047790},
           {.src = 2328584819, .dst = 2797090300, .length = 190630926},
           {.src = 351462117, .dst = 3278448653, .length = 7002746},
           {.src = 1277601137, .dst = 126959518, .length = 72076752},
           {.src = 465293361, .dst = 92351208, .length = 34608310},
           {.src = 3866348216, .dst = 4142640720, .length = 123572459},
           {.src = 1080416378, .dst = 2143980560, .length = 43307177},
           {.src = 2672287871, .dst = 1450895191, .length = 693085369},
           {.src = 3365373240, .dst = 517080586, .length = 114425963},
           {.src = 1662866566, .dst = 3388436971, .length = 411783072},
           {.src = 2654083387, .dst = 2187287737, .length = 18204484},
           {.src = 1650614172, .dst = 1417513852, .length = 12252394},
           {.src = 1349677889, .dst = 3067794208, .length = 210654445},
           {.src = 4202678943, .dst = 4266213179, .length = 28754117},
           {.src = 1123723555, .dst = 2653162718, .length = 96139859},
           {.src = 2519215745, .dst = 1071196524, .length = 99869466}},
};
const struct map water_light_map = {
  .srcname = "water",
  .dstname = "light",
  .map_count = 44,
  .maps = {{.src = 90187036, .dst = 512627839, .length = 1196629},
           {.src = 2059506154, .dst = 3379634653, .length = 33434334},
           {.src = 4276482087, .dst = 3286651054, .length = 18485209},
           {.src = 28914830, .dst = 4233695090, .length = 61272206},
           {.src = 3322576776, .dst = 3413068987, .length = 23288997},
           {.src = 3345865773, .dst = 3736304424, .length = 43267308},
           {.src = 2994853001, .dst = 1246285471, .length = 251748584},
           {.src = 1946298040, .dst = 3779571732, .length = 113208114},
           {.src = 3287769466, .dst = 390808412, .length = 34807310},
           {.src = 2879009693, .dst = 1881283842, .length = 106527924},
           {.src = 2506138169, .dst = 3964031050, .length = 12994476},
           {.src = 793897944, .dst = 3436357984, .length = 162691614},
           {.src = 2092940488, .dst = 2255160753, .length = 151061610},
           {.src = 3506201042, .dst = 853985057, .length = 119010035},
           {.src = 1856875022, .dst = 301385394, .length = 89423018},
           {.src = 658665705, .dst = 972995092, .length = 34308693},
           {.src = 1315925500, .dst = 4159948022, .length = 65322692},
           {.src = 250463411, .dst = 640912738, .length = 213072319},
           {.src = 91383665, .dst = 1761800914, .length = 102591221},
           {.src = 3246601585, .dst = 450345319, .length = 5793995},
           {.src = 4173678310, .dst = 3186220306, .length = 91115364},
           {.src = 3633635453, .dst = 28914830, .length = 176360375},
           {.src = 193974886, .dst = 456139314, .length = 56488525},
           {.src = 3809995828, .dst = 2523290324, .length = 187303152},
           {.src = 3389133081, .dst = 2406222363, .length = 117067961},
           {.src = 2782899504, .dst = 205275205, .length = 96110189},
           {.src = 1100569535, .dst = 2135785589, .length = 119375164},
           {.src = 533846267, .dst = 1121466033, .length = 124819438},
           {.src = 2244002098, .dst = 1007303785, .length = 114162248},
           {.src = 3997298980, .dst = 3599049598, .length = 137254826},
           {.src = 463535730, .dst = 4077949072, .length = 70310537},
           {.src = 3625211077, .dst = 4225270714, .length = 8424376},
           {.src = 2519132645, .dst = 1498034055, .length = 263766859},
           {.src = 1381248192, .dst = 2710593476, .length = 475626830},
           {.src = 692974398, .dst = 3977025526, .length = 100923546},
           {.src = 4264793674, .dst = 4148259609, .length = 11688413},
           {.src = 2358164346, .dst = 1987811766, .length = 147973823},
           {.src = 1244674296, .dst = 3892779846, .length = 71251204},
           {.src = 4134553806, .dst = 3340510149, .length = 39124504},
           {.src = 956589558, .dst = 1864392135, .length = 16891707},
           {.src = 1219944699, .dst = 425615722, .length = 24729597},
           {.src = 973481265, .dst = 513824468, .length = 127088270},
           {.src = 2985537617, .dst = 3277335670, .length = 9315384},
           {.src = 3252395580, .dst = 3305136263, .length = 35373886}},
};
const struct map light_temperature_map = {
  .srcname = "light",
  .dstname = "temperature",
  .map_count = 46,
  .maps = {{.src = 698410082, .dst = 1094191559, .length = 28110394},
           {.src = 1189042355, .dst = 383870732, .length = 107231661},
           {.src = 2164474756, .dst = 3711052230, .length = 34756304},
           {.src = 170241759, .dst = 745558539, .length = 7170863},
           {.src = 503970250, .dst = 491102393, .length = 194439832},
           {.src = 3142749029, .dst = 4034618875, .length = 146609939},
           {.src = 1718948669, .dst = 3781998432, .length = 129329785},
           {.src = 3071819711, .dst = 2440091414, .length = 70929318},
           {.src = 55123603, .dst = 1301358031, .length = 115118156},
           {.src = 2789116652, .dst = 0, .length = 87933685},
           {.src = 177412622, .dst = 770729148, .length = 48955790},
           {.src = 3886204605, .dst = 3772681560, .length = 9316872},
           {.src = 37123857, .dst = 752729402, .length = 17999746},
           {.src = 2137385460, .dst = 3745808534, .length = 7147939},
           {.src = 3677936618, .dst = 2028807236, .length = 208267987},
           {.src = 3289358968, .dst = 2237075223, .length = 92979022},
           {.src = 1960439220, .dst = 88764920, .length = 176946240},
           {.src = 2258695303, .dst = 3568470355, .length = 142581875},
           {.src = 1848278454, .dst = 3276170082, .length = 112160766},
           {.src = 1129503077, .dst = 2637902204, .length = 39814191},
           {.src = 892603630, .dst = 3000547589, .length = 188042422},
           {.src = 226368412, .dst = 2511020732, .length = 126881472},
           {.src = 1296274016, .dst = 1122301953, .length = 52818372},
           {.src = 1353023078, .dst = 1440958847, .length = 243104929},
           {.src = 0, .dst = 2963423732, .length = 37123857},
           {.src = 2199231060, .dst = 3388330848, .length = 48304954},
           {.src = 377732544, .dst = 1175120325, .length = 126237706},
           {.src = 1349092388, .dst = 819684938, .length = 3930690},
           {.src = 1169317268, .dst = 3752956473, .length = 19725087},
           {.src = 2144533399, .dst = 3911328217, .length = 19941357},
           {.src = 353249884, .dst = 1416476187, .length = 24482660},
           {.src = 3895521477, .dst = 2677716395, .length = 285707337},
           {.src = 2413138935, .dst = 265711160, .length = 118159572},
           {.src = 1080646052, .dst = 685542225, .length = 48857025},
           {.src = 2401277178, .dst = 3556608598, .length = 11861757},
           {.src = 2247536014, .dst = 734399250, .length = 11159289},
           {.src = 3677105383, .dst = 87933685, .length = 831235},
           {.src = 1596128007, .dst = 3188590011, .length = 87580071},
           {.src = 2531298507, .dst = 836373414, .length = 257818145},
           {.src = 2877050337, .dst = 3471876393, .length = 84732205},
           {.src = 726520476, .dst = 1684063776, .length = 166083154},
           {.src = 3560998296, .dst = 823615628, .length = 12757786},
           {.src = 1683708078, .dst = 3436635802, .length = 35240591},
           {.src = 3573756082, .dst = 3931269574, .length = 103349301},
           {.src = 3382337990, .dst = 1850146930, .length = 178660306},
           {.src = 2961782542, .dst = 2330054245, .length = 110037169}},
};
const struct map temperature_humidity_map = {
  .srcname = "temperature",
  .dstname = "humidity",
  .map_count = 27,
  .maps = {{.src = 4122818507, .dst = 1773059646, .length = 172148789},
           {.src = 2859734866, .dst = 2417158855, .length = 110076859},
           {.src = 1576624124, .dst = 977168274, .length = 28149321},
           {.src = 3797606290, .dst = 4275291678, .length = 19675618},
           {.src = 749646180, .dst = 1141296808, .length = 267286171},
           {.src = 2969811725, .dst = 3592756112, .length = 273274339},
           {.src = 19621130, .dst = 0, .length = 7167651},
           {.src = 2697725300, .dst = 2059084943, .length = 48133058},
           {.src = 3920609496, .dst = 2107218001, .length = 145140777},
           {.src = 1152911564, .dst = 1453481278, .length = 151292167},
           {.src = 1465584228, .dst = 1408582979, .length = 44898299},
           {.src = 0, .dst = 7167651, .length = 19621130},
           {.src = 1829621431, .dst = 2907567891, .length = 240604380},
           {.src = 3652347291, .dst = 2252358778, .length = 145258999},
           {.src = 1016932351, .dst = 1005317595, .length = 135979213},
           {.src = 2745858358, .dst = 1945208435, .length = 113876508},
           {.src = 4065750273, .dst = 2397617777, .length = 16506015},
           {.src = 1776094709, .dst = 3251499859, .length = 53526722},
           {.src = 4082256288, .dst = 2867005672, .length = 40562219},
           {.src = 1304203731, .dst = 26788781, .length = 161380497},
           {.src = 2409995769, .dst = 3305026581, .length = 287729531},
           {.src = 3243086064, .dst = 3866030451, .length = 409261227},
           {.src = 1773059646, .dst = 2414123792, .length = 3035063},
           {.src = 1510482527, .dst = 911026677, .length = 66141597},
           {.src = 3817281908, .dst = 3148172271, .length = 103327588},
           {.src = 2070225811, .dst = 2527235714, .length = 339769958},
           {.src = 26788781, .dst = 188169278, .length = 722857399}},
};
const struct map humidity_location_map = {
  .srcname = "humidity",
  .dstname = "location",
  .map_count = 28,
  .maps = {{.src = 3137303541, .dst = 3907319746, .length = 31421983},
           {.src = 1018495475, .dst = 3085093695, .length = 286155292},
           {.src = 2491485887, .dst = 2898003508, .length = 87665522},
           {.src = 2901838353, .dst = 2546787368, .length = 7997221},
           {.src = 2829836257, .dst = 3835317650, .length = 72002096},
           {.src = 3509894030, .dst = 2554784589, .length = 133012322},
           {.src = 3719561871, .dst = 3487595595, .length = 104747874},
           {.src = 2667334372, .dst = 3714670750, .length = 120646900},
           {.src = 2909835574, .dst = 975094571, .length = 227467967},
           {.src = 3864000834, .dst = 2985669030, .length = 99424665},
           {.src = 2449777255, .dst = 3672962118, .length = 41708632},
           {.src = 2787981272, .dst = 3631107133, .length = 41854985},
           {.src = 3963425499, .dst = 3938741729, .length = 15057061},
           {.src = 3824309745, .dst = 3447904506, .length = 39691089},
           {.src = 1304650767, .dst = 1824175159, .length = 641793976},
           {.src = 0, .dst = 242892183, .length = 6504921},
           {.src = 3642906352, .dst = 3371248987, .length = 76655519},
           {.src = 2258930589, .dst = 1698833898, .length = 81940357},
           {.src = 6504921, .dst = 0, .length = 242892183},
           {.src = 3978482560, .dst = 2465969135, .length = 80818233},
           {.src = 4256203632, .dst = 3592343469, .length = 38763664},
           {.src = 3168725524, .dst = 3953798790, .length = 341168506},
           {.src = 4134179998, .dst = 2775979874, .length = 122023634},
           {.src = 975094571, .dst = 1780774255, .length = 43400904},
           {.src = 1946444743, .dst = 1311468847, .length = 312485846},
           {.src = 2579151409, .dst = 2687796911, .length = 88182963},
           {.src = 2340870946, .dst = 1202562538, .length = 108906309},
           {.src = 4059300793, .dst = 1623954693, .length = 74879205}},
};

const struct map *maps[] = {
  &seed_soil_map,         &soil_fertilizer_map,      &fertilizer_water_map,  &water_light_map,
  &light_temperature_map, &temperature_humidity_map, &humidity_location_map,
};

unsigned long int process_seed(unsigned long int seed) {
  for (int i = 0; i < sizeof(maps) / sizeof(maps[0]); i++) {
    const struct map *map = maps[i];
    for (int j = 0; j < map->map_count; j++) {
      const struct map_entry *entry = &map->maps[j];
      if (entry->src <= seed && seed < entry->src + entry->length) {
        seed = entry->dst + (seed - entry->src);
        break;
      }
    }
  }
  return seed;
}

unsigned long int process_seed_range(unsigned long int seed, unsigned long int iterations) {
  unsigned long int min_location = __LONG_MAX__;
  for (int i = 0; i < iterations; i++) {
    unsigned long int location = process_seed(seed+i);
    min_location = location < min_location ? location : min_location;
  }
  return min_location;
}

// #define DEBUG_LOG(...) printf(__VA_ARGS__)
#define DEBUG_LOG(...)

void *process_seed_range_thread(void *arg) {
  unsigned long int *args = (unsigned long int *)arg;
  unsigned long int seed = args[0];
  unsigned long int iterations = args[1];
  unsigned long int *min_location = &args[2];
  *min_location = process_seed_range(seed, iterations);
  DEBUG_LOG("Thread finished, min was %ld\n", *min_location);
  return NULL;
}


int main(int argc, char **argv) {
  if (argc != 3) {
    printf("Usage: %s <seed> <iterations>\n", argv[0]);
    return 1;
  }

  // args are <start> <iterations>
  unsigned long int seed = strtol(argv[1], NULL, 10);
  unsigned long int iterations = strtol(argv[2], NULL, 10);

  // we need to split the work across all available cpu cores
  // we can do this by dividing the work into chunks and then
  // starting a thread for each chunk
  int cpu_count = sysconf(_SC_NPROCESSORS_ONLN);

  DEBUG_LOG("Using %d threads\n", cpu_count);

  // we need to divide the work into chunks
  unsigned long int chunk_size = iterations / cpu_count;
  unsigned long int remainder = iterations % cpu_count;

  // we need to start a thread for each chunk
  // each thread will process a chunk of the work
  // and return the minimum location
  struct thread_and_args {
    pthread_t thread;
    unsigned long int *args;
  };

  struct thread_and_args *threads_and_args = malloc(sizeof(struct thread_and_args) * cpu_count);

  for (int i = 0; i < cpu_count; i++) {
    unsigned long int start = i * chunk_size + seed;
    unsigned long int count = chunk_size;
    if (i == cpu_count - 1) {
      count += remainder;
    }

    DEBUG_LOG("Starting thread %d with start=%ld count=%ld\n", i, start, count);

    struct thread_and_args *thread_and_args = &threads_and_args[i];
    thread_and_args->args = malloc(sizeof(unsigned long int) * 3);
    thread_and_args->args[0] = start;
    thread_and_args->args[1] = count;

    pthread_create(&thread_and_args->thread, NULL, process_seed_range_thread, thread_and_args->args);
  }

  // wait for all threads to finish, grabbing min value from each
  unsigned long int min_location = __LONG_MAX__;

  for (int i = 0; i < cpu_count; i++) {
    pthread_t thread = threads_and_args[i].thread;
    pthread_join(thread, NULL);

    unsigned long int *args = threads_and_args[i].args;
    unsigned long int location = args[2];
    min_location = location < min_location ? location : min_location;
  }

  printf("%ld\n", min_location);
  return 0;
}
