import axiosInstance from '../utils/axiosInstance';
import Post from '../components/Post';

type HomeProps = {
  posts: Array<{
    id: number;
    title: string;
  }>;
};

const Home: React.FC<HomeProps> = ({ posts }) => (
  <table>
    <tbody>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </tbody>
  </table>
);

export async function getStaticProps() {
  const { data: posts } = await axiosInstance.get('/posts');
  return { props: { posts } };
}

export default Home;
